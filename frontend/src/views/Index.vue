<template>
    <div id="app">
        <div class="header-container">
            <h1>Africa CSIRTs Map</h1> 
            <RouterLink :to="{name:'add'}" class="button-green">Add new CSIRT</RouterLink>
        </div>
        <div class="search-filter">
            <input v-model="searchQuery" placeholder="Search for a CSIRT...">
        </div>
        <div id="map-container"></div>
        <csirt-list :csirts="filteredCSIRTs" @update-csirt="updateCSIRT" />
        <add-csirt-form @add-csirt="addCSIRT" />
    </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import L from 'leaflet';
// import CSIRTList from './components/CSIRTList.vue';
// import AddCSIRTForm from './components/AddCSIRTForm.vue';
import { fetchCSIRTs, updateCSIRT as updateCSIRTApi, addCSIRT as addCSIRTApi } from '../services/api.js';

export default {
    name: 'App',
    // components: {
    //   CSIRTList,
    //   AddCSIRTForm,
    // },
    setup() {
        const csirts = ref([]);
        const searchQuery = ref('');
        const map = ref(null);

        const filteredCSIRTs = computed(() => {
            return csirts.value.filter(csirt =>
                csirt.name.toLowerCase().includes(searchQuery.value.toLowerCase())
            );
        });

        const loadCSIRTs = async () => {
            try {
                csirts.value = await fetchCSIRTs();
                console.log(csirts.value);
                updateMap();
            } catch (error) {
                console.error('Error fetching CSIRTs:', error);
            }
        };

        const updateMap = () => {
            if (map.value) {
                map.value.eachLayer((layer) => {
                    if (layer instanceof L.Marker) {
                        map.value.removeLayer(layer);
                    }
                });

                csirts.value.forEach(csirt => {
                    L.marker([csirt.latitude, csirt.longitude])
                        .addTo(map.value)
                        .bindPopup(csirt.name);
                });
            }
        };

        const updateCSIRT = async (updatedCSIRT) => {
            try {
                const result = await updateCSIRTApi(updatedCSIRT);
                const index = csirts.value.findIndex(c => c.id === result.id);
                if (index !== -1) {
                    csirts.value[index] = result;
                }
                updateMap();
            } catch (error) {
                console.error('Error updating CSIRT:', error);
            }
        };

        const addCSIRT = async (newCSIRT) => {
            try {
                const result = await addCSIRTApi(newCSIRT);
                csirts.value.push(result);
                updateMap();
            } catch (error) {
                console.error('Error adding CSIRT:', error);
            }
        };

        onMounted(() => {
            map.value = L.map('map-container').setView([0, 20], 3);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map.value);

            loadCSIRTs();
        });

        return {
            csirts,
            searchQuery,
            filteredCSIRTs,
            updateCSIRT,
            addCSIRT,
        };
    },
};
</script>

<style>
#app {
    font-family: Arial, sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

#map-container {
    height: 500px;
    margin-bottom: 20px;
}

.search-filter {
    margin-bottom: 20px;
}

input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
}

.button-green {
    background-color: #28a745; 
    color: white;
    padding: 10px 20px;
    border: none;  
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 16px;
    transition: background-color 0.3s ease;
}

.button-green:hover {
    background-color: #218838;
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
</style>