from agents import Agent, Runner, trace, InputGuardrailTripwireTriggered
from agents.guardrail import input_guardrail, GuardrailFunctionOutput
from agents.items import TResponseInputItem
from connection import config
from pydantic import BaseModel
from typing import Union
import asyncio
import rich

# Output model for Luggage Agent
class Luggage(BaseModel):
    reasoning: str
    isWeightExceed: bool
# Luggage Agent
luggage_agent = Agent(
    name="Luggage Agent",
    instructions="""
    Yor are an agent that keeps track of weight of passenger luggage.If customer carries luggage more than 25kg say no to user politely
    """,
    output_type=Luggage
    )
# Guardrail Function
@input_guardrail
async def luggage_guardrail(ctx, agent: Agent, input: Union[str | list]):
    result = await Runner.run(luggage_agent, input, run_config=config, context=ctx)
    rich.print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.isWeightExceed)
# Security Agent (with guardrail)
security_agent = Agent(
    name="Security Agent",
    instructions="""
    You are a security agent. Your task is to keep check passenger before onboarding them on the plane.
     """,
    input_guardrails=[luggage_guardrail],
    )
# Main Function
async def main():
    with trace("PassengerLuggageGuardrail"):
        try:
            result = await Runner.run(security_agent, "My luggage weight is 30kg", run_config=config)
            rich.print(result)
            rich.print("[green]Guardrail did not trip[/green]")
        except InputGuardrailTripwireTriggered:
            rich.print("[red]Guardrail tripped: You cannt check in with more than 25kg.[/red]")

if __name__ == "__main__":
    asyncio.run(main())
