from rest_framework import serializers

from webapp.models import Project, Task, Type, State


class TypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True, allow_blank=False)

    class Meta:
        model = Type
        fields = (
            'id',
            'name'
        )
        read_only_fields = (
            'id',
        )


class StateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True, allow_blank=False)

    class Meta:
        model = State
        fields = (
            'id',
            'name'
        )
        read_only_fields = (
            'id',
        )


class TaskSerializer(serializers.ModelSerializer):
    state = StateSerializer(many=True)
    type = TypeSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'summary',
            'description',
            'created_at',
            'updated_at',
            'state',
            'type'
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )

    def update(self, instance, validated_data):
        instance.summary = validated_data.get('summary')
        instance.description = validated_data.get('description')

        state_data = validated_data.pop('state')
        instance.state.clear()
        instance.save()
        if state_data:
            for state_d in state_data:
                state = State(name=state_d.get('name'))
                state.save()
                instance.state.add(state)
        elif not state_data:
            state = State(name='Новая')
            state.save()
            instance.state.add(state)

        type_data = validated_data.pop('type')
        instance.type.clear()
        instance.save()
        if type_data:
            for type_d in type_data:
                type = Type(name=type_d.get('name'))
                type.save()
                instance.type.add(type)
        elif not type_data:
            type = Type(name='Задача')
            type.save()
            instance.type.add(type)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'date_start',
            'date_end'
        )
        read_only_fields = (
            'id',
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.date_start = validated_data.get('date_start')
        instance.date_end = validated_data.get('date_end')
        instance.save()

        return instance
