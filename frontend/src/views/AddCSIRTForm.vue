<template>
    <div class="add-csirt-form">
        <h2>Add New CSIRT</h2>
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="name">Name:</label>
                <input id="name" v-model="newCSIRT.name" placeholder="Enter CSIRT name" required
                    @blur="validateField('name')">
                <span class="error" v-if="errors.name">{{ errors.name }}</span>
            </div>

            <div class="form-group">
                <label for="contact_email">Email:</label>
                <input id="contact_email" v-model="newCSIRT.contact_email" placeholder="Enter CSIRT Email" required
                    @blur="validateField('contact_email')">
                <span class="error" v-if="errors.contact_email">{{ errors.contact_email }}</span>
            </div>

            <div class="form-group">
                <label for="location">Adresse:</label>
                <input id="location" v-model="newCSIRT.location" placeholder="Enter CSIRT Adresse" required
                    @blur="validateField('location')">
                <span class="error" v-if="errors.location">{{ errors.location }}</span>
            </div>

            <div class="form-group">
                <label for="country">Country:</label>
                <input id="country" v-model="newCSIRT.country" placeholder="Enter country" required
                    @blur="validateField('country')">
                <span class="error" v-if="errors.country">{{ errors.country }}</span>
            </div>

            <div class="form-group">
                <label for="latitude">Latitude:</label>
                <input id="latitude" v-model.number="newCSIRT.latitude" placeholder="Enter latitude" required
                    type="number" step="any" @blur="validateField('latitude')">
                <span class="error" v-if="errors.latitude">{{ errors.latitude }}</span>
            </div>

            <div class="form-group">
                <label for="longitude">Longitude:</label>
                <input id="longitude" v-model.number="newCSIRT.longitude" placeholder="Enter longitude" required
                    type="number" step="any" @blur="validateField('longitude')">
                <span class="error" v-if="errors.longitude">{{ errors.longitude }}</span>
            </div>

            <div class="form-group">
                <label for="description">Description:</label>
                <textarea id="description" v-model="newCSIRT.description" placeholder="Enter a brief description"
                    @blur="validateField('description')"></textarea>
                <span class="error" v-if="errors.description">{{ errors.description }}</span>
            </div>

            <button type="submit" :disabled="!isFormValid || loading">
                <span v-if="loading" class="spinner"></span>
                <span v-if="!loading">Add CSIRT</span>
            </button>
        </form>
    </div>
</template>

<script>
import { reactive, computed, ref } from 'vue';
import { addCSIRT as addCSIRTApi } from '../services/api.js';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default {
    name: 'AddCSIRTForm',
    emits: ['add-csirt'],
    setup(props, { emit }) {
        const loading = ref(false);
        const newCSIRT = reactive({
            name: '',
            country: '',
            latitude: null,
            longitude: null,
            description: '',
            contact_email: '',
            location: ''
        });

        const errors = reactive({
            name: '',
            country: '',
            latitude: '',
            longitude: '',
            description: '',
            contact_email: '',
            location: ''
        });

        const validateEmail = (email) => {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        };

        const validateField = (field) => {
            errors[field] = '';
            switch (field) {
                case 'name':
                    if (newCSIRT.name.length < 2) {
                        errors.name = 'Name must be at least 2 characters long';
                    }
                    break;
                case 'country':
                    if (newCSIRT.country.length < 2) {
                        errors.country = 'Country must be at least 2 characters long';
                    }
                    break;
                case 'latitude':
                    if (newCSIRT.latitude < -90 || newCSIRT.latitude > 90) {
                        errors.latitude = 'Latitude must be between -90 and 90';
                    }
                    break;
                case 'longitude':
                    if (newCSIRT.longitude < -180 || newCSIRT.longitude > 180) {
                        errors.longitude = 'Longitude must be between -180 and 180';
                    }
                    break;
                case 'description':
                    if (newCSIRT.description.length > 500) {
                        errors.description = 'Description must be 500 characters or less';
                    }
                    break;
                case 'contact_email':
                    if (!validateEmail(newCSIRT.email)) {
                        errors.email = 'Invalid email format';
                    }
                    break;
            }
        };

        const isFormValid = computed(() => {
            return (
                newCSIRT.name &&
                newCSIRT.country &&
                newCSIRT.latitude !== null &&
                newCSIRT.longitude !== null &&
                newCSIRT.contact_email !== null &&
                newCSIRT.location !== null &&
                !Object.values(errors).some(error => error !== '')
            );
        });

        const submitForm = async () => {
            if (isFormValid.value) {
                try {
                    loading.value = true;

                    console.log(loading.value)
                    console.log(loading.value)
                    console.log(loading.value)
                    console.log(loading.value)
                    console.log(loading.value)
                    console.log(loading.value)
                    console.log(loading.value)
                    console.log(loading.value)
                    const response = await addCSIRTApi({
                        name: newCSIRT.name,
                        country: newCSIRT.country,
                        latitude: newCSIRT.latitude,
                        longitude: newCSIRT.longitude,
                        description: newCSIRT.description,
                        contact_email: newCSIRT.contact_email,
                        location: newCSIRT.location
                    });
                    console.log('CSIRT added:', response.data);
                    emit('add-csirt', response.data);
                    toast("CSIRT inserted successfully.", {
                        autoClose: 5000,
                    });

                    // Reset form after successful submission
                    Object.assign(newCSIRT, {
                        name: '',
                        country: '',
                        latitude: null,
                        longitude: null,
                        description: '',
                        contact_email: '',
                        location: ''
                    });
                } catch (error) {
                    console.error('Error adding CSIRT:', error);
                } finally {
                    loading.value = false; 
                }
            }
        };

        return {
            newCSIRT,
            errors,
            validateField,
            isFormValid,
            submitForm,
        };
    },
};
</script>

<style scoped>
.add-csirt-form {
    max-width: 500px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

h2 {
    text-align: center;
    color: #333;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input,
textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
}

textarea {
    height: 100px;
    resize: vertical;
}

button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}

button:hover:not(:disabled) {
    background-color: #45a049;
}

.spinner {
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-top: 3px solid white;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

.error {
    color: red;
    font-size: 12px;
    margin-top: 5px;
    display: block;
}
</style>