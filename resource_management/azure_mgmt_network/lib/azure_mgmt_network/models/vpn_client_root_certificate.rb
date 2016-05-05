# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Network
  module Models
    #
    # VPN client root certificate of virtual network gateway
    #
    class VpnClientRootCertificate < MsRestAzure::SubResource

      include MsRestAzure

      # @return [VpnClientRootCertificatePropertiesFormat]
      attr_accessor :properties

      # @return [String] Gets name of the resource that is unique within a
      # resource group. This name can be used to access the resource
      attr_accessor :name

      # @return [String] A unique read-only string that changes whenever the
      # resource is updated
      attr_accessor :etag

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

        serialized_property = object.properties
        unless serialized_property.nil?
          serialized_property = VpnClientRootCertificatePropertiesFormat.serialize_object(serialized_property)
        end
        output_object['properties'] = serialized_property unless serialized_property.nil?

        serialized_property = object.name
        output_object['name'] = serialized_property unless serialized_property.nil?

        serialized_property = object.etag
        output_object['etag'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [VpnClientRootCertificate] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = VpnClientRootCertificate.new

        deserialized_property = object['id']
        output_object.id = deserialized_property

        deserialized_property = object['properties']
        unless deserialized_property.nil?
          deserialized_property = VpnClientRootCertificatePropertiesFormat.deserialize_object(deserialized_property)
        end
        output_object.properties = deserialized_property

        deserialized_property = object['name']
        output_object.name = deserialized_property

        deserialized_property = object['etag']
        output_object.etag = deserialized_property

        output_object
      end
    end
  end
end
