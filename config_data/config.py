from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot():
    token: str


@dataclass
class Config():
    tg_bot: TgBot


def load_config(path_to_env: str) -> Config:
    env: Env = Env()
    env.read_env(path=path_to_env)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))