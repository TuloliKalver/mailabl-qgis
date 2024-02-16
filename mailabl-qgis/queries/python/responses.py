
class handleResponse:
    @staticmethod
    def handle_properties_response(self, response):
        data = response.json()
        #print(f"data = {data}")
        fetched_data = data.get("data", {}).get("properties", {}).get("edges", [])
        #print(f"fetched data = {fetched_data}")
        pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
        #print(f"Page info = {pageInfo}")
        end_cursor = pageInfo.get("endCursor")
        #print(f"end_cursor = {end_cursor}")
        last_page = pageInfo.get("lastPage")
        #print(f"last_page = {last_page}")
        return data, fetched_data, pageInfo, end_cursor, last_page

    @staticmethod
    def response_data_json(self, response):
        data_json = response.json()
        #print(f"data = {data_json}")
        return data_json
    
    @staticmethod
    def response_properties_data_edges(response):
        data = response.json()
        fetched_data = data.get("data", {}).get("properties", {}).get("edges", [])
        #print(f"fetched data = {fetched_data}")
        return fetched_data
    
    @staticmethod        
    def response_properties_data_ids(response):
        data = response.json()
        # Check if the required keys are present in the JSON
        if 'data' in data and 'properties' in data['data'] and 'edges' in data['data']['properties']:
            # Extract IDs from the JSON
            ids = [edge['node']['id'] for edge in data['data']['properties']['edges']]
            # Print the extracted IDs
            #print("Extracted IDs:")
            #print(ids)
            return ids
    
    @staticmethod        
    def response_properties_cadastral_numbers(response):
        data = response.json()
        # Check if the required keys are present in the JSON
        if 'data' in data and 'properties' in data['data'] and 'edges' in data['data']['properties']:
            # Extract IDs from the JSON
            cadastral_units = [edge['node']['cadastralUnit'] for edge in data['data']['properties']['edges']]
            #print(cadastral_units)
              # Extract numbers from cadastral units
            numbers = [unit['number'] for unit in cadastral_units]
            # Print the extracted IDs
            #print("Extracted IDs:")
            #print(ids)
            return numbers
    
    
    @staticmethod
    def response_properties_pageInfo(response):
        data = response.json()
        pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
        #print(f"Page info = {pageInfo}")
        return pageInfo
    
    @staticmethod
    def response_properties_endCursor(response):
        pageInfo = handleResponse.response_properties_pageInfo(response)
        end_cursor = pageInfo.get("endCursor")
        #print(f"end_cursor = {end_cursor}")
        return end_cursor

    @staticmethod    
    def response_properties_lastPage(response):
        pageInfo = handleResponse.response_properties_pageInfo(response)
        last_page = pageInfo.get("lastPage")
        #print(f"last_page = {last_page}")
        return last_page
