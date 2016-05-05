# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Graph
  module Models
    #
    # Active Directory object information
    #
    class AADObject

      include MsRestAzure

      # @return [String] Gets or sets object Id
      attr_accessor :object_id

      # @return [String] Gets or sets object type
      attr_accessor :object_type

      # @return [String] Gets or sets object display name
      attr_accessor :display_name

      # @return [String] Gets or sets principal name
      attr_accessor :user_principal_name

      # @return [String] Gets or sets mail
      attr_accessor :mail

      # @return [Boolean] Gets or sets MailEnabled field
      attr_accessor :mail_enabled

      # @return [Boolean] Gets or sets SecurityEnabled field
      attr_accessor :security_enabled

      # @return [String] Gets or sets signIn name
      attr_accessor :sign_in_name

      # @return [Array<String>] Gets or sets the list of service principal
      # names.
      attr_accessor :service_principal_names

      # @return [String] Gets or sets the user type
      attr_accessor :user_type

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @service_principal_names.each{ |e| e.validate if e.respond_to?(:validate) } unless @service_principal_names.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.object_id
        output_object['objectId'] = serialized_property unless serialized_property.nil?

        serialized_property = object.object_type
        output_object['objectType'] = serialized_property unless serialized_property.nil?

        serialized_property = object.display_name
        output_object['displayName'] = serialized_property unless serialized_property.nil?

        serialized_property = object.user_principal_name
        output_object['userPrincipalName'] = serialized_property unless serialized_property.nil?

        serialized_property = object.mail
        output_object['mail'] = serialized_property unless serialized_property.nil?

        serialized_property = object.mail_enabled
        output_object['mailEnabled'] = serialized_property unless serialized_property.nil?

        serialized_property = object.security_enabled
        output_object['securityEnabled'] = serialized_property unless serialized_property.nil?

        serialized_property = object.sign_in_name
        output_object['signInName'] = serialized_property unless serialized_property.nil?

        serialized_property = object.service_principal_names
        output_object['servicePrincipalNames'] = serialized_property unless serialized_property.nil?

        serialized_property = object.user_type
        output_object['userType'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [AADObject] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = AADObject.new

        deserialized_property = object['objectId']
        output_object.object_id = deserialized_property

        deserialized_property = object['objectType']
        output_object.object_type = deserialized_property

        deserialized_property = object['displayName']
        output_object.display_name = deserialized_property

        deserialized_property = object['userPrincipalName']
        output_object.user_principal_name = deserialized_property

        deserialized_property = object['mail']
        output_object.mail = deserialized_property

        deserialized_property = object['mailEnabled']
        output_object.mail_enabled = deserialized_property

        deserialized_property = object['securityEnabled']
        output_object.security_enabled = deserialized_property

        deserialized_property = object['signInName']
        output_object.sign_in_name = deserialized_property

        deserialized_property = object['servicePrincipalNames']
        output_object.service_principal_names = deserialized_property

        deserialized_property = object['userType']
        output_object.user_type = deserialized_property

        output_object
      end
    end
  end
end
