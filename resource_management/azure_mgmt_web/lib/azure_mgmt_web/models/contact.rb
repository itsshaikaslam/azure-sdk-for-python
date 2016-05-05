# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Contact information for domain registration. If 'Domain Privacy' option
    # is not selected then the contact information will be  be made publicly
    # available through the Whois directories as per ICANN requirements.
    #
    class Contact

      include MsRestAzure

      # @return [Address] Mailing address
      attr_accessor :address_mailing

      # @return [String] Email address
      attr_accessor :email

      # @return [String] Fax number
      attr_accessor :fax

      # @return [String] Job title
      attr_accessor :job_title

      # @return [String] First name
      attr_accessor :name_first

      # @return [String] Last name
      attr_accessor :name_last

      # @return [String] Middle name
      attr_accessor :name_middle

      # @return [String] Organization
      attr_accessor :organization

      # @return [String] Phone number
      attr_accessor :phone

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @address_mailing.validate unless @address_mailing.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.address_mailing
        unless serialized_property.nil?
          serialized_property = Address.serialize_object(serialized_property)
        end
        output_object['addressMailing'] = serialized_property unless serialized_property.nil?

        serialized_property = object.email
        output_object['email'] = serialized_property unless serialized_property.nil?

        serialized_property = object.fax
        output_object['fax'] = serialized_property unless serialized_property.nil?

        serialized_property = object.job_title
        output_object['jobTitle'] = serialized_property unless serialized_property.nil?

        serialized_property = object.name_first
        output_object['nameFirst'] = serialized_property unless serialized_property.nil?

        serialized_property = object.name_last
        output_object['nameLast'] = serialized_property unless serialized_property.nil?

        serialized_property = object.name_middle
        output_object['nameMiddle'] = serialized_property unless serialized_property.nil?

        serialized_property = object.organization
        output_object['organization'] = serialized_property unless serialized_property.nil?

        serialized_property = object.phone
        output_object['phone'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [Contact] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = Contact.new

        deserialized_property = object['addressMailing']
        unless deserialized_property.nil?
          deserialized_property = Address.deserialize_object(deserialized_property)
        end
        output_object.address_mailing = deserialized_property

        deserialized_property = object['email']
        output_object.email = deserialized_property

        deserialized_property = object['fax']
        output_object.fax = deserialized_property

        deserialized_property = object['jobTitle']
        output_object.job_title = deserialized_property

        deserialized_property = object['nameFirst']
        output_object.name_first = deserialized_property

        deserialized_property = object['nameLast']
        output_object.name_last = deserialized_property

        deserialized_property = object['nameMiddle']
        output_object.name_middle = deserialized_property

        deserialized_property = object['organization']
        output_object.organization = deserialized_property

        deserialized_property = object['phone']
        output_object.phone = deserialized_property

        output_object
      end
    end
  end
end
