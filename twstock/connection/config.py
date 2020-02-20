from dataclasses import dataclass

@dataclass
class ConnectionConfig: # pylint: disable=too-many-instance-attributes
    # HashedControlPassword for TOR
    password: str = ""
    # ControlPort in TOR (default: 9051)
    port: int = 9051
