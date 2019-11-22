from flask import request, current_app
from flask_restplus import Namespace, Resource

from backend.dataServices import SensorDataService
from backend.token_auth import auth_needed

api = Namespace("sensor", description="Expose sensor Data")


@api.route("/data/<int:page_size>/<int:page>")
@api.route("/data/<int:page_size>/<int:page>/<string:order>")
class SensorResource(Resource):
    def get(self, page_size, page, order="desc"):
        if page_size < 0 or page < 0:
            return dict(message="page_size and page must be positive integers"), 400
        if page_size > 500:
            return dict(message="page_size limit 500")
        return SensorDataService().get_sensor_data(page_size, page, order)


@api.route("/collector/<app_key>/<net_key>/<device_id>/")
class CollectorResource(Resource):
    def get(self, app_key, net_key, device_id):
        try:
            SensorDataService().insert_many_from_http(
                app_key, net_key, device_id, request.args.to_dict()
            )
        except Exception as e:
            return (
                dict(
                    message=f"something went wrong trying to insert values with http  error:{e.args[0]}"
                ),
                500,
            )

        return dict(message="success")
