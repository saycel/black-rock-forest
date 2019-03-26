from app.database import Base
from sqlalchemy import Column, Integer, String


class Data(Base):
    __tablename__ = 'sensordata'
    id = Column(Integer, autoincrement='auto', primary_key=True)
    sensor_id = Column(Integer)
    value = Column(Integer)
    unit = Column(String(3))

    def __init__(self, sensor_id, value, unit):
        self.sensor_id = sensor_id
        self.value = value
        self.unit = unit

    def decode(self, payload):
        try:
            self.__init__(payload.get('sensor_id'),
                          payload.get('value'),
                          payload.get('unit'))
        except Exception:
            return dict(message='bad record')

    def __repr__(self):
        return f'<Sensor {self.sensor_id}>'

    @property
    def serialize(self):
        return dict(sensor_id=self.sensor_id, 
                    value=self.value, 
                    unit=self.unit)
