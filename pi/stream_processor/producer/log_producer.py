from pi import KafkaProducerClient


class LogProducer(object):
    # TODO: Implement parallel processing
    producer = KafkaProducerClient()
    for idx in range(1000):
        data = {
            "res": {
                "body": {
                    "success": False,
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "There is an error trying to process your transaction at the moment. Please try again in a while.",
                    "data": {}
                },
                "_headers": {
                    "set-cookie": "id-mercury=; Path=/apis/v1; Expires=Thu, 01 Jan 1970 00:00:00 GMT",
                    "x-accel-buffering": "no",
                    "access-control-allow-headers": "undefined",
                    "access-control-allow-credentials": "true",
                    "access-control-expose-headers": "id-mercury",
                    "x-server-timestamp": "1559037314590",
                    "content-type": "application/json; charset=utf-8",
                    "content-length": "167",
                    "etag": "W/\"a7-e+mYDAtUpp7U59+za+6pr7UE294\"",
                    "x-response-time": "97.723ms"
                }
            },
            "req": {
                "body": {
                    "merchantId": "MORESUPERMARKET",
                    "transactionId": "12781910260852152512",
                    "merchantOrderId": "1278-1910260852",
                    "amount": 28208,
                    "instrumentType": "MOBILE",
                    "instrumentReference": "9154548181",
                    "message": "Collect for Order Id:1278-1910260852",
                    "email": "",
                    "expiresIn": 180,
                    "shortName": "",
                    "subMerchant": "",
                    "storeId": "1278",
                    "terminalId": "J1910"
                },
                "headers": {
                    "host": "mercury.traefik.prod.phonepe.com",
                    "user-agent": "Go-http-client/1.1",
                    "content-length": "454",
                    "content-type": "application/json",
                    "x-client-ip": "103.39.0.112",
                    "x-forwarded-by": "103.243.35.246:443",
                    "x-forwarded-for": "103.39.0.112, 10.85.22.27",
                    "x-forwarded-host": "mercury.traefik.prod.phonepe.com",
                    "x-forwarded-port": "80",
                    "x-forwarded-proto": "http",
                    "x-forwarded-server": "prd-traefik101",
                    "x-real-ip": "10.85.22.27",
                    "x-verify": "1ca27036776dbb3d41316e13b82b046e50d8bf3d9d2e96ebc473076f8ab18d11",
                    "accept-encoding": "gzip",
                    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJwaG9uZXBlLWFwaSIsImV4cCI6MzMwODcxODQ2MzgsImlhdCI6MTUzMDI3NTgzOCwic3ViIjoiTU9SRVNVUEVSTUFSS0VUIiwicm9sZSI6Im1lcmNoYW50IiwidHlwZSI6InN0YXRpYyJ9.106JWEJDuEKEpb0VodD_F5JTbjUoi6O8JHGWz0T4N2CE9gm4_MIoJnq69J5MB0ZEqpNtD-XcwNl6m2Va5IKjFA",
                    "x-salt-index": "1",
                    "x-auth-mode": "dummy"
                }
            },
            "responseTime": 98
        }
        producer.send_message(data=data)
