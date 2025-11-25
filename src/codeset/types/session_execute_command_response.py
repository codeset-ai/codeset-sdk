# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SessionExecuteCommandResponse"]


class SessionExecuteCommandResponse(BaseModel):
    interaction_id: str
    """Unique identifier for the interaction."""

    status: str
    """Status of the interaction: 'pending', 'processing', 'completed', or 'failed'."""
