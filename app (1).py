from opentelemetry import trace 
from flask import Flask, request 
from opentelemetry.sdk.resources import Resource 
from opentelemetry.sdk.trace import TracerProvider 
from opentelemetry.sdk.trace.export import BatchSpanProcessor 
from random import randint 
from opentelemetry.sdk.trace.export import ConsoleSpanExporter 
app = Flask(__name__) 
provider = TracerProvider() 
processor = BatchSpanProcessor(ConsoleSpanExporter()) 
provider.add_span_processor(processor) 
trace.set_tracer_provider(provider) 
tracer = trace.get_tracer(__name__) 

# below


@app.route("/roll") 
def roll(): 
  with tracer.start_as_current_span( 
    "server_request",  
    attributes={ "endpoint": "/roll" }  
  ):
    sides = int(request.args.get('sides')) 
    rolls = int(request.args.get('rolls')) 
    return roll_sum(sides,rolls)  

def roll_sum(sides, rolls): 
  span = trace.get_current_span() 
  sum = 0 
  for r in range(0,rolls): 
    result = randint(1,sides) 
    span.add_event( "log", { 
      "roll.sides": sides, 
      "roll.result": result, 
    })
    sum += result 
  return  str(sum) 