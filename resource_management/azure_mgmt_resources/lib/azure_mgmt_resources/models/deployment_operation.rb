# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Resources
  module Models
    #
    # Deployment operation information.
    #
    class DeploymentOperation

      include MsRestAzure

      # @return [String] Gets or sets full deployment operation id.
      attr_accessor :id

      # @return [String] Gets or sets deployment operation id.
      attr_accessor :operation_id

      # @return [DeploymentOperationProperties] Gets or sets deployment
      # properties.
      attr_accessor :properties

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @properties.validate unless @properties.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.id
        output_object['id'] = serialized_property unless serialized_property.nil?

        serialized_property = object.operation_id
        output_object['operationId'] = serialized_property unless serialized_property.nil?

        serialized_property = object.properties
        unless serialized_property.nil?
          serialized_property = DeploymentOperationProperties.serialize_object(serialized_property)
        end
        output_object['properties'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [DeploymentOperation] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = DeploymentOperation.new

        deserialized_property = object['id']
        output_object.id = deserialized_property

        deserialized_property = object['operationId']
        output_object.operation_id = deserialized_property

        deserialized_property = object['properties']
        unless deserialized_property.nil?
          deserialized_property = DeploymentOperationProperties.deserialize_object(deserialized_property)
        end
        output_object.properties = deserialized_property

        output_object
      end
    end
  end
end
