# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StreamSet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'time': 'TimeStream',
        'distance': 'DistanceStream',
        'latlng': 'LatLngStream',
        'altitude': 'AltitudeStream',
        'velocity_smooth': 'SmoothVelocityStream',
        'heartrate': 'HeartrateStream',
        'cadence': 'CadenceStream',
        'watts': 'PowerStream',
        'temp': 'TemperatureStream',
        'moving': 'MovingStream',
        'grade_smooth': 'SmoothGradeStream'
    }

    attribute_map = {
        'time': 'time',
        'distance': 'distance',
        'latlng': 'latlng',
        'altitude': 'altitude',
        'velocity_smooth': 'velocity_smooth',
        'heartrate': 'heartrate',
        'cadence': 'cadence',
        'watts': 'watts',
        'temp': 'temp',
        'moving': 'moving',
        'grade_smooth': 'grade_smooth'
    }

    def __init__(self, time=None, distance=None, latlng=None, altitude=None, velocity_smooth=None, heartrate=None, cadence=None, watts=None, temp=None, moving=None, grade_smooth=None):  # noqa: E501
        """StreamSet - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._distance = None
        self._latlng = None
        self._altitude = None
        self._velocity_smooth = None
        self._heartrate = None
        self._cadence = None
        self._watts = None
        self._temp = None
        self._moving = None
        self._grade_smooth = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if distance is not None:
            self.distance = distance
        if latlng is not None:
            self.latlng = latlng
        if altitude is not None:
            self.altitude = altitude
        if velocity_smooth is not None:
            self.velocity_smooth = velocity_smooth
        if heartrate is not None:
            self.heartrate = heartrate
        if cadence is not None:
            self.cadence = cadence
        if watts is not None:
            self.watts = watts
        if temp is not None:
            self.temp = temp
        if moving is not None:
            self.moving = moving
        if grade_smooth is not None:
            self.grade_smooth = grade_smooth

    @property
    def time(self):
        """Gets the time of this StreamSet.  # noqa: E501


        :return: The time of this StreamSet.  # noqa: E501
        :rtype: TimeStream
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StreamSet.


        :param time: The time of this StreamSet.  # noqa: E501
        :type: TimeStream
        """

        self._time = time

    @property
    def distance(self):
        """Gets the distance of this StreamSet.  # noqa: E501


        :return: The distance of this StreamSet.  # noqa: E501
        :rtype: DistanceStream
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this StreamSet.


        :param distance: The distance of this StreamSet.  # noqa: E501
        :type: DistanceStream
        """

        self._distance = distance

    @property
    def latlng(self):
        """Gets the latlng of this StreamSet.  # noqa: E501


        :return: The latlng of this StreamSet.  # noqa: E501
        :rtype: LatLngStream
        """
        return self._latlng

    @latlng.setter
    def latlng(self, latlng):
        """Sets the latlng of this StreamSet.


        :param latlng: The latlng of this StreamSet.  # noqa: E501
        :type: LatLngStream
        """

        self._latlng = latlng

    @property
    def altitude(self):
        """Gets the altitude of this StreamSet.  # noqa: E501


        :return: The altitude of this StreamSet.  # noqa: E501
        :rtype: AltitudeStream
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """Sets the altitude of this StreamSet.


        :param altitude: The altitude of this StreamSet.  # noqa: E501
        :type: AltitudeStream
        """

        self._altitude = altitude

    @property
    def velocity_smooth(self):
        """Gets the velocity_smooth of this StreamSet.  # noqa: E501


        :return: The velocity_smooth of this StreamSet.  # noqa: E501
        :rtype: SmoothVelocityStream
        """
        return self._velocity_smooth

    @velocity_smooth.setter
    def velocity_smooth(self, velocity_smooth):
        """Sets the velocity_smooth of this StreamSet.


        :param velocity_smooth: The velocity_smooth of this StreamSet.  # noqa: E501
        :type: SmoothVelocityStream
        """

        self._velocity_smooth = velocity_smooth

    @property
    def heartrate(self):
        """Gets the heartrate of this StreamSet.  # noqa: E501


        :return: The heartrate of this StreamSet.  # noqa: E501
        :rtype: HeartrateStream
        """
        return self._heartrate

    @heartrate.setter
    def heartrate(self, heartrate):
        """Sets the heartrate of this StreamSet.


        :param heartrate: The heartrate of this StreamSet.  # noqa: E501
        :type: HeartrateStream
        """

        self._heartrate = heartrate

    @property
    def cadence(self):
        """Gets the cadence of this StreamSet.  # noqa: E501


        :return: The cadence of this StreamSet.  # noqa: E501
        :rtype: CadenceStream
        """
        return self._cadence

    @cadence.setter
    def cadence(self, cadence):
        """Sets the cadence of this StreamSet.


        :param cadence: The cadence of this StreamSet.  # noqa: E501
        :type: CadenceStream
        """

        self._cadence = cadence

    @property
    def watts(self):
        """Gets the watts of this StreamSet.  # noqa: E501


        :return: The watts of this StreamSet.  # noqa: E501
        :rtype: PowerStream
        """
        return self._watts

    @watts.setter
    def watts(self, watts):
        """Sets the watts of this StreamSet.


        :param watts: The watts of this StreamSet.  # noqa: E501
        :type: PowerStream
        """

        self._watts = watts

    @property
    def temp(self):
        """Gets the temp of this StreamSet.  # noqa: E501


        :return: The temp of this StreamSet.  # noqa: E501
        :rtype: TemperatureStream
        """
        return self._temp

    @temp.setter
    def temp(self, temp):
        """Sets the temp of this StreamSet.


        :param temp: The temp of this StreamSet.  # noqa: E501
        :type: TemperatureStream
        """

        self._temp = temp

    @property
    def moving(self):
        """Gets the moving of this StreamSet.  # noqa: E501


        :return: The moving of this StreamSet.  # noqa: E501
        :rtype: MovingStream
        """
        return self._moving

    @moving.setter
    def moving(self, moving):
        """Sets the moving of this StreamSet.


        :param moving: The moving of this StreamSet.  # noqa: E501
        :type: MovingStream
        """

        self._moving = moving

    @property
    def grade_smooth(self):
        """Gets the grade_smooth of this StreamSet.  # noqa: E501


        :return: The grade_smooth of this StreamSet.  # noqa: E501
        :rtype: SmoothGradeStream
        """
        return self._grade_smooth

    @grade_smooth.setter
    def grade_smooth(self, grade_smooth):
        """Sets the grade_smooth of this StreamSet.


        :param grade_smooth: The grade_smooth of this StreamSet.  # noqa: E501
        :type: SmoothGradeStream
        """

        self._grade_smooth = grade_smooth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StreamSet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StreamSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
