from fastapi import FastAPI
from app.api import router
from app.terminology_api import router as terminology_router
from app.email_service import router as email_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

#from app.demo_api import router as demo_router
#from app.contribute_api import router as contribution_router
#from app.dashboards.contributor_dashboard import router as contributor_dashboard_router
#from dotenv import load_dotenv
#from app.auth.auth_api import router as auth_router
#from slowapi.errors import RateLimitExceeded
#from slowapi.middleware import SlowAPIMiddleware
#from fastapi.responses import PlainTextResponse
#from app.middleware.rate_limit import limiter


#from app.datasets.parallel_dataset import ParallelDataset




app = FastAPI(
    title="Haitian Creole ⇄ English Public Translation API",
    description="Safe, standardized, domain-aware Haitian Creole translation",
    version="1.0.0"
)
load_dotenv()
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://kreyolapi.org",
        "https://www.kreyolapi.org",
        "https://api.kreyolapi.org",
        # Only allowed in dev mode
        #"http://localhost:8000",
        #"http://localhost:8080",
        #"http://localhost:3000",      
        #"http://localhost:5000",
        #"http://127.0.0.1:8000",
        #"http://127.0.0.1:8080",
        #"http://127.0.0.1:3000",
        #"http://127.0.0.1:5000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def root():
    return {
        "service": "Kreyol Translation API",
        "status": "running",
        "health": "/health",
        "docs": "/docs",
    }
"""@app.get("/")
def root():
    return {
        "message": "Welcome",
        "demo": "/demo",
        "contribute": "/contribute",
        "contributors_dashboard": "/dashboard/contributors",
        "docs": "/docs"
    }
"""
@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}
"""
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return PlainTextResponse(
        "Too many requests. Please slow down.",
        status_code=429
    )"""

app.include_router(router, prefix="/v1")
app.include_router(terminology_router, prefix="/v1")
#app.include_router(router)
app.include_router(email_router) 

# 🔑 THIS IS WHAT MAKES ROUTES EXIST
#app.include_router(translation_router)
#app.include_router(demo_router)
#app.include_router(contribution_router)
#app.include_router(contributor_dashboard_router)
#app.include_router(auth_router)
#app.include_router(test_demo, prefix="/v1")