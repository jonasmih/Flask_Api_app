"""empty message

Revision ID: eda4a77ce551
Revises: 
Create Date: 2021-01-23 23:03:53.916619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eda4a77ce551'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creditcardnumber', sa.Integer(), nullable=True),
    sa.Column('cardholder', sa.String(length=20), nullable=False),
    sa.Column('expirationdate', sa.Integer(), nullable=True),
    sa.Column('securitycode', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    # ### end Alembic commands ###