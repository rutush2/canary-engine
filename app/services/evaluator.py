import hashlib

class EngineEvaluator:
    @staticmethod
    def calculate_canary_allocation(user_id: str, flag_key: str) -> int:
        hash_input = f"{flag_key}:{user_id}".encode("utf-8")
        hash_digest = hashlib.md5(hash_input).hexdigest()
        hash_integer = int(hash_digest[:8], 16)
        return hash_integer % 100

    @classmethod
    def evaluate(cls, flag_model, user_id: str, context: dict) -> bool:
        if not flag_model.is_enabled:
            return False

        if flag_model.targeting_rules:
            for key, expected_value in flag_model.targeting_rules.items():
                user_value = context.get(key)
                if user_value != expected_value:
                    return False

        if flag_model.rollout_percentage >= 100:
            return True
        if flag_model.rollout_percentage <= 0:
            return False

        assigned_bucket = cls.calculate_canary_allocation(user_id, flag_model.key)
        return assigned_bucket < flag_model.rollout_percentage