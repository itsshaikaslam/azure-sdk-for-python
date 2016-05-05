# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Resources
  module Models
    #
    # Model object.
    #
    class ResourceManagementError

      include MsRestAzure

      # @return [String] Gets or sets the error code returned from the server.
      attr_accessor :code

      # @return [String] Gets or sets the error message returned from the
      # server.
      attr_accessor :message

      # @return [String] Gets or sets the target of the error.
      attr_accessor :target

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        fail MsRest::ValidationError, 'property code is nil' if @code.nil?
        fail MsRest::ValidationError, 'property message is nil' if @message.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.code
        output_object['code'] = serialized_property unless serialized_property.nil?

        serialized_property = object.message
        output_object['message'] = serialized_property unless serialized_property.nil?

        serialized_property = object.target
        output_object['target'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [ResourceManagementError] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = ResourceManagementError.new

        deserialized_property = object['code']
        output_object.code = deserialized_property

        deserialized_property = object['message']
        output_object.message = deserialized_property

        deserialized_property = object['target']
        output_object.target = deserialized_property

        output_object
      end
    end
  end
end
