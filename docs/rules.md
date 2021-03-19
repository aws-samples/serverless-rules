Rules
=====

## AWS Lambda

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Warning | [Lambda Tracing](lambda.md#tracing)                                 | WS1000   | Y      |
| Error   | [EventSourceMapping Failure Destination](lambda.md#eventsourcemapping-failure-destination) | ES1001   |        |
| Warning | Lambda Permission Principals                                        | WS1002   |        |
| Warning | Lambda Star Permissions                                             | WS1003   |        |
| Warning | Lambda Log Retention                                                | WS1004   |        |
| Error   | Lambda Deprecated Runtime                                           |          |        |
| Error   | Lambda No Error Alarm                                               |          |        |
| Error   | Async Lambda No Failure Destination                                 |          |        |
| Warning | Sync Lambda No Duration Alarm                                       |          |        |
| Warning | Sync Lambda With Destination                                        |          |        |
| Error   | SQS Lambda ReservedConcurrency < 5                                  |          |        |

## Amazon API Gateway REST APIs

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Error   | [API Gateway Logging](api_gateway.md#logging)                       | ES2000   | Y      |
| Warning | [API Gateway Structured Logging](api_gateway.md#structured-logging) | WS2001   |        |
| Warning | [API Gateway Tracing](api_gateway.md#tracing)                       | WS2002   | Y      |
| Warning | [API Gateway Default Throttling](api_gateway.md#default-throttling) | ES2003   |        |

## Amazon API Gateway HTTP APIs

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Error   | [API Gateway Logging](api_gateway.md#logging)                       | ES2000   | Y      |
| Warning | [API Gateway Structured Logging](api_gateway.md#structured-logging) | WS2001   |        |
| Warning | [API Gateway Default Throttling](api_gateway.md#default-throttling) | ES2003   | Y      |

## AWS AppSync

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Error   | AppSync Tracing                                                     | WS3000   | Y      |

## Amazon EventBridge

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Error   | EventBridge Rule No DLQ                                             | ES4000   |        |
| Info    | EventBridge Bus No Rule                                             |          |        |

## Amazon Step Functions

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Warning | Step Functions Tracing                                              | WS5000   |        |

## Amazon SQS

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Error   | SQS Queue No DLQ                                                    |          |        |

## Amazon SNS

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
