"""initial tables

Revision ID: 3da341156762
Revises: 
Create Date: 2024-11-13 07:52:15.416124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3da341156762'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(), nullable=False),
    sa.Column('last_name', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('mobile_phone', sa.VARCHAR(), nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('employee_logs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('log_in_time', sa.Time(), nullable=True),
    sa.Column('log_out_time', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('log_in_time'),
    sa.UniqueConstraint('log_out_time')
    )
    op.create_index(op.f('ix_employee_logs_user_id'), 'employee_logs', ['user_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_logs_user_id'), table_name='employee_logs')
    op.drop_table('employee_logs')
    op.drop_table('users')
    # ### end Alembic commands ###