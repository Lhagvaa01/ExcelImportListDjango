from rest_framework import serializers
from .models import *
from collections import OrderedDict

class VoicherPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoicherPrice
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    TCUSERICON = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Users
        fields = '__all__'


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductList
        fields = '_all_'

    def to_representation(self, instance):
        ordered_representation = OrderedDict([
            ("pk", instance.pk),
            ("TCITEMCODE", instance.TCITEMCODE),
            ("TCNAME", instance.TCNAME),
            ("TCGROUP", instance.TCGROUP),
            ("TCSALEPRICE", instance.TCSALEPRICE),
            ("TCVOUCHERPRICEPk", f"{instance.TCVOUCHERPRICEPk.name}" if instance.TCVOUCHERPRICEPk.name else None),
            ("TCBARCODE", instance.TCBARCODE),

        ])

        return ordered_representation
    