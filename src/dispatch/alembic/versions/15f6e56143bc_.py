"""Adds conversation to the incident type data model

Revision ID: 15f6e56143bc
Revises: 996dea17749b
Create Date: 2021-01-14 12:25:22.521667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "15f6e56143bc"
down_revision = "996dea17749b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("incident_type", sa.Column("conversation", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("incident_type", "conversation")
    # ### end Alembic commands ###
