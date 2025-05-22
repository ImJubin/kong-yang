import requests
from django.conf import settings
from .models import DepositProduct, DepositOption, SavingsProduct
from django.conf import settings

api_key = settings.FSS_API_KEY

def fetch_and_save_deposit_products():
    # 기존 예금 상품 전체 삭제
    DepositProduct.objects.all().delete()

    # 예금 조회 요청 URL
    url = "https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    params = {
        "auth": api_key,
        # 권역코드(은행)
        "topFinGrpNo": "020000",
        # api page
        "pageNo": 1  
    }

    response = requests.get(url, params=params)
    data = response.json()
    # 상품 종류
    base_list = data["result"]["baseList"]
    # 상품 옵션들
    option_list = data["result"]["optionList"]


    for product_data in base_list:
        product = DepositProduct.objects.create(
            # 금융상품 코드
            fin_prdt_cd = product_data["fin_prdt_cd"],
            # 금융회사 명
            kor_co_nm = product_data["kor_co_nm"],
            # 금융 상품명
            fin_prdt_nm = product_data["fin_prdt_nm"],
            # 가입 방법
            join_way = product_data["join_way"],
            # 가입대상
            join_member = product_data["join_member"],
            # 기타 유의사항
            etc_note = product_data.get("etc_note"),
            # 우대조건
            spcl_cnd = product_data.get("spcl_cnd"),
            # 최고한도
            max_limit = product_data.get("max_limit"),
            # 공시 제출월 [YYYYMM]
            dcls_month = product_data["dcls_month"]
        )

        for option_data in option_list:
            # product_data
            if option_data["fin_prdt_cd"] == product.fin_prdt_cd:
                DepositOption.objects.create(
                    deposit_product=product,
                    # 저축 기간 [단위: 개월]
                    save_trm=int(option_data["save_trm"]),
                    # 저축 금리 [소수점 2자리]
                    intr_rate=option_data.get("intr_rate"),
                    # 최고 우대금리 [소수점 2자리]
                    intr_rate2=option_data.get("intr_rate2"),
                    # 저축 금리 유형명
                    intr_rate_type_nm=option_data.get("intr_rate_type_nm", "")
                )


#################################################################################

def fetch_and_save_saving_products():
    # 기존 적금 상품 전체 삭제
    SavingsProduct.objects.all().delete()

    # 예금 조회 요청 URL
    url = "https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    params = {
        "auth": api_key,
        # 권역코드(은행)
        "topFinGrpNo": "020000",
        # api page
        "pageNo": 1  
    }

    response = requests.get(url, params=params)
    data = response.json()
    # 상품 종류
    base_list = data["result"]["baseList"]
    # 상품 옵션들
    option_list = data["result"]["optionList"]


    for product_data in base_list:
        product = DepositProduct.objects.create(
            # 금융상품 코드
            fin_prdt_cd = product_data["fin_prdt_cd"],
            # 금융회사 명
            kor_co_nm = product_data["kor_co_nm"],
            # 금융 상품명
            fin_prdt_nm = product_data["fin_prdt_nm"],
            # 가입 방법
            join_way = product_data["join_way"],
            # 가입대상
            join_member = product_data["join_member"],
            # 기타 유의사항
            etc_note = product_data.get("etc_note"),
            # 우대조건
            spcl_cnd = product_data.get("spcl_cnd"),
            # 최고한도
            max_limit = product_data.get("max_limit"),
            # 공시 제출월 [YYYYMM]
            dcls_month = product_data["dcls_month"]
        )

        for option_data in option_list:
            # product_data
            if option_data["fin_prdt_cd"] == product.fin_prdt_cd:
                DepositOption.objects.create(
                    deposit_product=product,
                    # 저축 기간 [단위: 개월]
                    save_trm=int(option_data["save_trm"]),
                    # 저축 금리 [소수점 2자리]
                    intr_rate=option_data.get("intr_rate"),
                    # 최고 우대금리 [소수점 2자리]
                    intr_rate2=option_data.get("intr_rate2"),
                    # 저축 금리 유형명
                    intr_rate_type_nm=option_data.get("intr_rate_type_nm", "")
                )
