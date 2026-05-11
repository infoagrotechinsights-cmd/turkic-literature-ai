from core.foundation_model import foundation_reasoning


class Orchestrator:

    def __init__(self):
        pass

    def run(self, poem: str):

        if not poem or not isinstance(poem, str):
            return {
                "error": "Invalid input"
            }

        # =========================
        # SINGLE SOURCE OF TRUTH
        # =========================
        foundation = foundation_reasoning(poem)

        return {
            "intertext": foundation.get("intertext", []),
            "alignment": foundation.get("alignment", {}),
            "motifs": foundation.get("motifs", []),
            "citations": foundation.get("citations", [])
        }
