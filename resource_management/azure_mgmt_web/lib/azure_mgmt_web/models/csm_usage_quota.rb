# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Usage of the quota resource
    #
    class CsmUsageQuota

      include MsRestAzure

      # @return [String] Units of measurement for the quota resourse
      attr_accessor :unit

      # @return [DateTime] Next reset time for the resource counter
      attr_accessor :next_reset_time

      # @return [Integer] The current value of the resource counter
      attr_accessor :current_value

      # @return [Integer] The resource limit
      attr_accessor :limit

      # @return [LocalizableString] Quota name
      attr_accessor :name

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @name.validate unless @name.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.unit
        output_object['unit'] = serialized_property unless serialized_property.nil?

        serialized_property = object.next_reset_time
        serialized_property = serialized_property.new_offset(0).strftime('%FT%TZ')
        output_object['nextResetTime'] = serialized_property unless serialized_property.nil?

        serialized_property = object.current_value
        output_object['currentValue'] = serialized_property unless serialized_property.nil?

        serialized_property = object.limit
        output_object['limit'] = serialized_property unless serialized_property.nil?

        serialized_property = object.name
        unless serialized_property.nil?
          serialized_property = LocalizableString.serialize_object(serialized_property)
        end
        output_object['name'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [CsmUsageQuota] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = CsmUsageQuota.new

        deserialized_property = object['unit']
        output_object.unit = deserialized_property

        deserialized_property = object['nextResetTime']
        deserialized_property = DateTime.parse(deserialized_property) unless deserialized_property.to_s.empty?
        output_object.next_reset_time = deserialized_property

        deserialized_property = object['currentValue']
        deserialized_property = Integer(deserialized_property) unless deserialized_property.to_s.empty?
        output_object.current_value = deserialized_property

        deserialized_property = object['limit']
        deserialized_property = Integer(deserialized_property) unless deserialized_property.to_s.empty?
        output_object.limit = deserialized_property

        deserialized_property = object['name']
        unless deserialized_property.nil?
          deserialized_property = LocalizableString.deserialize_object(deserialized_property)
        end
        output_object.name = deserialized_property

        output_object
      end
    end
  end
end
