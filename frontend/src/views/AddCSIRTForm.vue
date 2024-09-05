<template>
    <div class="add-csirt-form">
        <h2>Add New CSIRT</h2>
        <form @submit.prevent="submitForm">
            <input v-model="newCSIRT.name" placeholder="Name" required>
            <input v-model="newCSIRT.country" placeholder="Country" required>
            <input v-model.number="newCSIRT.latitude" placeholder="Latitude" required type="number" step="any">
            <input v-model.number="newCSIRT.longitude" placeholder="Longitude" required type="number" step="any">
            <button type="submit" class="button-green">Add CSIRT</button>
        </form>
    </div>
</template>

<script>
import { reactive } from 'vue';
import { addCSIRT as addCSIRTApi } from '../services/api.js';

export default {
    name: 'AddCSIRTForm',
    emits: ['add-csirt'],
    setup() {
        const newCSIRT = reactive({
            name: '',
            country: '',
            latitude: null,
            longitude: null,
        });

        const submitForm = async (newCSIRT) => {
            try {
                await addCSIRTApi(newCSIRT);
            } catch (error) {
                console.error('Error adding CSIRT:', error);
            }
        };

        return {
            newCSIRT,
            submitForm,
        };
    },
};
</script>

<style scoped>
.add-csirt-form {
    margin-top: 20px;
}

form {
    display: flex;
    flex-direction: column;
}

input {
    margin-bottom: 10px;
    padding: 5px;
}

button {
    align-self: flex-start;
}
</style>