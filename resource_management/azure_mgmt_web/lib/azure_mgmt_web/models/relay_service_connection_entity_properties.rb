# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Model object.
    #
    class RelayServiceConnectionEntityProperties

      include MsRestAzure

      # @return [String]
      attr_accessor :entity_name

      # @return [String]
      attr_accessor :entity_connection_string

      # @return [String]
      attr_accessor :resource_type

      # @return [String]
      attr_accessor :resource_connection_string

      # @return [String]
      attr_accessor :hostname

      # @return [Integer]
      attr_accessor :port

      # @return [String]
      attr_accessor :biztalk_uri

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

        serialized_property = object.entity_name
        output_object['entityName'] = serialized_property unless serialized_property.nil?

        serialized_property = object.entity_connection_string
        output_object['entityConnectionString'] = serialized_property unless serialized_property.nil?

        serialized_property = object.resource_type
        output_object['resourceType'] = serialized_property unless serialized_property.nil?

        serialized_property = object.resource_connection_string
        output_object['resourceConnectionString'] = serialized_property unless serialized_property.nil?

        serialized_property = object.hostname
        output_object['hostname'] = serialized_property unless serialized_property.nil?

        serialized_property = object.port
        output_object['port'] = serialized_property unless serialized_property.nil?

        serialized_property = object.biztalk_uri
        output_object['biztalkUri'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [RelayServiceConnectionEntityProperties] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = RelayServiceConnectionEntityProperties.new

        deserialized_property = object['entityName']
        output_object.entity_name = deserialized_property

        deserialized_property = object['entityConnectionString']
        output_object.entity_connection_string = deserialized_property

        deserialized_property = object['resourceType']
        output_object.resource_type = deserialized_property

        deserialized_property = object['resourceConnectionString']
        output_object.resource_connection_string = deserialized_property

        deserialized_property = object['hostname']
        output_object.hostname = deserialized_property

        deserialized_property = object['port']
        deserialized_property = Integer(deserialized_property) unless deserialized_property.to_s.empty?
        output_object.port = deserialized_property

        deserialized_property = object['biztalkUri']
        output_object.biztalk_uri = deserialized_property

        output_object
      end
    end
  end
end
