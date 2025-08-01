✅ Objective:
The goal of this code is to simulate an AI-based airport luggage checking system using guardrails. It ensures that passengers do not bring luggage exceeding 25kg by using a guardrail mechanism that blocks such inputs before allowing the user to board (handled by the Security Agent).

Working Flow:

Passenger input goes to the Security Agent.

Before processing, it is intercepted by the luggage_guardrail.

The Luggage Agent analyzes if the weight exceeds the allowed limit.

If >25kg, the guardrail trips, and the action is blocked.

If ≤25kg, the request proceeds to the Security Agent.



https://github.com/user-attachments/assets/14893526-b812-4b55-b08a-cf5e919fd841

<img width="1609" height="906" alt="SecurityAgent" src="https://github.com/user-attachments/assets/41994a90-56b0-4312-b18c-f1f30bd13ce8" />
<img width="1608" height="904" alt="luggage-IO" src="https://github.com/user-attachments/assets/4439ed16-2578-4f6f-9a70-2816a06311cd" />
<img width="1608" height="905" alt="LuggageAgent" src="https://github.com/user-attachments/assets/5c21b8b8-10f5-4d1c-8c4e-f45ba93fc733" />
<img width="1610" height="906" alt="luggageGuardrail" src="https://github.com/user-attachments/assets/59ea4760-653a-446a-8224-f1be2557fd34" />
<img width="1609" height="904" alt="PassengerGuardrail2" src="https://github.com/user-attachments/assets/f9632824-3e4f-4f09-99b9-bc9993c6f010" />
<img width="1611" height="905" alt="PassengerGuardrail 1" src="https://github.com/user-attachments/assets/c3caa30f-c250-420f-b2e4-db5ba7d254be" />




