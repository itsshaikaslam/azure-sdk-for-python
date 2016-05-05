# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Authorization
  module Models
    #
    # Resource Type
    #
    class ResourceType

      include MsRestAzure

      # @return [String] Gets or sets the resource type name
      attr_accessor :name

      # @return [String] Gets or sets the resource type display name
      attr_accessor :display_name

      # @return [Array<ProviderOperation>] Gets or sets the resource type
      # operations
      attr_accessor :operations

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @operations.each{ |e| e.validate if e.respond_to?(:validate) } unless @operations.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.name
        output_object['name'] = serialized_property unless serialized_property.nil?

        serialized_property = object.display_name
        output_object['displayName'] = serialized_property unless serialized_property.nil?

        serialized_property = object.operations
        unless serialized_property.nil?
          serializedArray = []
          serialized_property.each do |element|
            unless element.nil?
              element = ProviderOperation.serialize_object(element)
            end
            serializedArray.push(element)
          end
          serialized_property = serializedArray
        end
        output_object['operations'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [ResourceType] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = ResourceType.new

        deserialized_property = object['name']
        output_object.name = deserialized_property

        deserialized_property = object['displayName']
        output_object.display_name = deserialized_property

        deserialized_property = object['operations']
        unless deserialized_property.nil?
          deserialized_array = []
          deserialized_property.each do |element1|
            unless element1.nil?
              element1 = ProviderOperation.deserialize_object(element1)
            end
            deserialized_array.push(element1)
          end
          deserialized_property = deserialized_array
        end
        output_object.operations = deserialized_property

        output_object
      end
    end
  end
end
