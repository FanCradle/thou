import requests
import json

# Base URLs
LOCAL_BASE = "http://127.0.0.1:5328/api"
CLOUD_BASE = "https://nft-backend-service-71622892890.us-central1.run.app/api"

# Sample payload
collection_payload = {
    "name": "Test Collection",
    "symbol": "TST",
    "royaltyFeeNumerator": 250,
    "maxSupply": 10000,
    "maxPerWallet": 10,
    "contractURI": "/ipfs/sample_contract_uri.json"
}

mint_payload = {
    "toAddress": "0x2Dd13e22f842e965a262554E534274BE00cb2c5d",
    "tokenURI": "ipfs/sample_token_uri.json"
}

def test_health_check(base):
    r = requests.get(f"{base}/collections/health")
    print("Health Check:", r.status_code, r.json())

def test_create_collection(base):
    r = requests.post(f"{base}/collections/create", json=collection_payload)
    print("Create Collection:", r.status_code, r.json())
    return r.json().get("collectionAddress")  # Adjust depending on response schema

def test_get_all_collections(base):
    r = requests.get(f"{base}/collections/")
    print("All Collections:", r.status_code, r.json())

def test_get_by_creator(base, creator_address):
    r = requests.get(f"{base}/collections/creator/{creator_address}")
    print("Collections by Creator:", r.status_code, r.json())

def test_get_by_address(base, collection_address):
    r = requests.get(f"{base}/collections/{collection_address}")
    print("Get by Address:", r.status_code, r.json())

def test_validate_collection(base, collection_address):
    r = requests.get(f"{base}/collections/{collection_address}/validate")
    print("Validate Collection:", r.status_code, r.json())

def test_mint(base, collection_address):
    r = requests.post(f"{base}/collections/{collection_address}/mint", json=mint_payload)
    print("Mint to Collection:", r.status_code, r.json())

def run_all_tests(base):
    print(f"\nTesting base: {base}\n" + "-"*40)
    test_health_check(base)
    collection_address = test_create_collection(base)
    if collection_address:
        test_get_by_address(base, collection_address)
        test_validate_collection(base, collection_address)
        test_mint(base, collection_address)
    test_get_all_collections(base)
    test_get_by_creator(base, mint_payload["toAddress"])

# Run tests on local and cloud
# run_all_tests(LOCAL_BASE)
run_all_tests(CLOUD_BASE)
