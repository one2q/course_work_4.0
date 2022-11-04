"""add user.favorite_genre

Revision ID: d1587989119c
Revises: 9e3b672853f1
Create Date: 2022-10-29 11:11:58.791504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1587989119c'
down_revision = '9e3b672853f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_genre', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'genre', ['favorite_genre'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('favorite_genre')

    # ### end Alembic commands ###
