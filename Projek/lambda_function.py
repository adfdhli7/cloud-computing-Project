import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ErrorAuditLogs')

def lambda_handler(event, context):
    # Mengurai pesan dari SNS
    sns_message = event['Records'][0]['Sns']['Message']
    
    try:
        alarm_data = json.loads(sns_message)
        alarm_name = alarm_data.get('AlarmName', 'Unknown Alarm')
        reason = alarm_data.get('NewStateReason', 'No reason provided')
    except json.JSONDecodeError:
        # Jika pesan bukan format JSON (misal saat tes manual)
        alarm_name = "Manual SNS Test"
        reason = sns_message
    
    # Menyiapkan data untuk audit trail
    item = {
        'LogID': str(uuid.uuid4()),
        'Timestamp': datetime.now().isoformat(),
        'AlarmName': alarm_name,
        'Reason': reason,
        'Status': 'CRITICAL_ERROR'
    }
    
    # Memasukkan baris data (item) baru di tabel Amazon DynamoDB
    table.put_item(Item=item)
    
    print(f"Log berhasil disimpan: {item['LogId']}")
    return {
        "statusCode": 200, 
        "body": json.dumps("Audit log saved successfully")
    }