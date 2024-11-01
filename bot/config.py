from dataclasses import dataclass

@dataclass
class RedisSettings:
    host: str = 'redis'
    port: str = '5858'
    db:   int = 1


@dataclass
class PostgresSettings:
    pass
