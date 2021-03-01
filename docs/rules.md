Rules
=====

## AWS Lambda

| Level   | Name                                       | cfn-lint | tflint |
|---------|--------------------------------------------|----------|--------|
| Error   | [Lambda Tracing](lambda.md#tracing) | ES1000   | N      |

## Amazon API Gateway

| Level   | Name                                                                | cfn-lint | tflint |
|---------|---------------------------------------------------------------------|----------|--------|
| Error   | [API Gateway Logging](api_gateway.md#logging)                       | ES2000   | Y      |
| Warning | [API Gateway Structured Logging](api_gateway.md#structured-logging) | WS2001   | N      |
| Error   | [API Gateway Tracing](api_gateway.md#tracing)                       | ES2002   | Y      |

