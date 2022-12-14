"""category table

Revision ID: d3c1c6eaea88
Revises: 
Create Date: 2022-09-11 22:11:36.332624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3c1c6eaea88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('logo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stock_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('total_cost', sa.Float(), nullable=True),
    sa.Column('cur_status', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=64), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('cost_transport_per_mile', sa.Float(), nullable=True),
    sa.Column('service_charge', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('momo_number', sa.String(length=20), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('thing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unique_name', sa.String(length=64), nullable=True),
    sa.Column('shelf_life', sa.Integer(), nullable=True),
    sa.Column('electric_consumption', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unique_name')
    )
    op.create_table('utility_meter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('recharge_amount', sa.String(length=64), nullable=True),
    sa.Column('treshold_amount', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utility_meter')
    op.drop_table('thing')
    op.drop_table('supplier')
    op.drop_table('stock')
    op.drop_table('order_details')
    op.drop_table('device')
    op.drop_table('category')
    op.drop_table('brand')
    # ### end Alembic commands ###
