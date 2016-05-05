# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Class repesenting metrics availability and retention
    #
    class MetricAvailabilily

      include MsRestAzure

      # @return [String] Time grain
      attr_accessor :time_grain

      # @return [String] Retention period for the current
      # {Microsoft.Web.Hosting.Administration.MetricAvailabilily.TimeGrain}
      attr_accessor :retention

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        # Nothing to validate
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.time_grain
        output_object['timeGrain'] = serialized_property unless serialized_property.nil?

        serialized_property = object.retention
        output_object['retention'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [MetricAvailabilily] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = MetricAvailabilily.new

        deserialized_property = object['timeGrain']
        output_object.time_grain = deserialized_property

        deserialized_property = object['retention']
        output_object.retention = deserialized_property

        output_object
      end
    end
  end
end
