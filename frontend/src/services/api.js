import axios from 'axios';

const API_URL = 'https://cyberspector-api.nickfal.com/api';

export const fetchCSIRTs = async () => {
    const response = await axios.get(`${API_URL}/csirts`);
    return response.data.data;
};

export const updateCSIRT = async (csirt) => {
    const response = await axios.put(`${API_URL}/csirts/${csirt.id}`, csirt);
    return response.data;
};

export const addCSIRT = async (csirt) => {
    const response = await axios.post(`${API_URL}/csirts/`, csirt);
    return response.data;
};