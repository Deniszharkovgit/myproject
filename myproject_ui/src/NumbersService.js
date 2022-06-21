import axios from 'axios';
const API_URL = 'http://0.0.0.0:8000/api/numbers';

export default class CustomersService{

	constructor(){}


	getNumbers() {
		const url = `${API_URL}`;
		return axios.get(url).then(response => response.data);
	}
}
