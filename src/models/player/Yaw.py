from src.models.player.Justine import Justine


class Yaw(Justine):

    @staticmethod
    def _get_player_info() -> str:
        return str("Yaw")

    def get_name(self):
        return super().get_name()
