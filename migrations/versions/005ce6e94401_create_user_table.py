"""create user table

Revision ID: 005ce6e94401
Revises:
Create Date: 2021-02-16 16:17:14.968184

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '005ce6e94401'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('password', sa.Unicode(length=255), nullable=False),
        sa.Column('email', sa.Unicode(length=255), nullable=False),
        sa.Column('nickname', sa.Unicode(length=255), nullable=False),
        sa.Column('is_admin', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('nickname'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###