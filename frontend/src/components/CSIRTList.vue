<template>
    <div class="csirt-list">
        <h2>CSIRTs</h2>
        <ul>
            <li v-for="csirt in csirts" :key="csirt.id">
                {{ csirt.name }} ({{ csirt.country }})
                <button @click="editCSIRT(csirt)">Edit</button>
            </li>
        </ul>
        <div v-if="editingCSIRT" class="edit-form">
            <h3>Edit CSIRT</h3>
            <input v-model="editingCSIRT.name" placeholder="Name">
            <input v-model="editingCSIRT.country" placeholder="Country">
            <input v-model.number="editingCSIRT.latitude" placeholder="Latitude">
            <input v-model.number="editingCSIRT.longitude" placeholder="Longitude">
            <button @click="saveEdit">Save</button>
            <button @click="cancelEdit">Cancel</button>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: 'CSIRTList',
    props: {
        csirts: Array,
    },
    emits: ['update-csirt'],
    setup(props, { emit }) {
        const editingCSIRT = ref(null);

        const editCSIRT = (csirt) => {
            editingCSIRT.value = { ...csirt };
        };

        const saveEdit = () => {
            emit('update-csirt', editingCSIRT.value);
            editingCSIRT.value = null;
        };

        const cancelEdit = () => {
            editingCSIRT.value = null;
        };

        return {
            editingCSIRT,
            editCSIRT,
            saveEdit,
            cancelEdit,
        };
    },
};
</script>

<style scoped>
.csirt-list {
    margin-top: 20px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

.edit-form {
    margin-top: 20px;
}

input {
    display: block;
    margin-bottom: 10px;
}
</style>