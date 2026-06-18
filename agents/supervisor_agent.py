class SupervisorAgent:

    def validate(
        self,
        risk
    ):

        if risk == "HIGH":

            return (
                "Immediate SOC escalation required."
            )

        return (
            "Standard monitoring recommended."
        )
