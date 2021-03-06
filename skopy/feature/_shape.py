import uuid

import sqlalchemy

from ._base import Base


class Shape(Base):
    __tablename__ = "shapes"

    area = sqlalchemy.Column(sqlalchemy.Float)

    axis_major = sqlalchemy.Column(sqlalchemy.Float)
    axis_minor = sqlalchemy.Column(sqlalchemy.Float)

    convex_area = sqlalchemy.Column(sqlalchemy.Integer)

    eccentricity = sqlalchemy.Column(sqlalchemy.Float)

    equivalent_diameter = sqlalchemy.Column(sqlalchemy.Float)

    euler_number = sqlalchemy.Column(sqlalchemy.Integer)

    extent = sqlalchemy.Column(sqlalchemy.Float)

    orientation = sqlalchemy.Column(sqlalchemy.Float)

    perimeter = sqlalchemy.Column(sqlalchemy.Float)

    solidity = sqlalchemy.Column(sqlalchemy.Float)

    @staticmethod
    def measure(properties):
        parameters = {
            "area": properties.area,
            "axis_major": properties.major_axis_length,
            "axis_minor": properties.minor_axis_length,
            "convex_area": properties.convex_area,
            "eccentricity": properties.eccentricity,
            "equivalent_diameter": properties.equivalent_diameter,
            "euler_number": properties.euler_number,
            "extent": properties.extent,
            "id": uuid.uuid4(),
            "orientation": properties.orientation,
            "perimeter": properties.perimeter,
            "solidity": properties.solidity
        }

        return Shape(**parameters)
