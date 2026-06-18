from workflows.incident_workflow import (
    run_incident_workflow
)

print("=" * 60)
print("CyberIntelAI")
print("=" * 60)

alert = input(
    "\nEnter Security Alert:\n"
)

result = run_incident_workflow(
    alert
)

print("\n")
print("=" * 60)

print("CLASSIFICATION")
print(result["classification"])

print("\nRISK")
print(result["risk"])

print("\nMITRE")
print(result["mitre"])

print("\nIOCS")
print(result["iocs"])

print("\nREPORT")
print(result["report"])
