import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class AirportsService:
    name = "airports_service"

    redis = Redis('development')

    # Now the struture is following
    # airport_id: {
    #     airport: string,
    #     trips: array
    # }


    @rpc
    def get(self, airport_id):
        airport = self.redis.get(airport_id)
        print(airport)
        return airport

    @rpc
    def create(self, airport):
        airport_id = uuid.uuid4().hex
        print("aaaaaaaaaaaaaaaaaaaaaaaaa")
        self.redis.hmset(airport_id, {
            'airport': airport,
            'trips': None
        })
        return airport_id
