# In-memory data storage (replaces PostgreSQL)

from datetime import datetime
from typing import List, Optional, Dict
import json

# In-memory data stores
services_db: List[Dict] = []
contacts_db: List[Dict] = []
demos_db: List[Dict] = []
patches_db: List[Dict] = []

# Auto-increment counters
service_id_counter = 1
contact_id_counter = 1
demo_id_counter = 1
patch_id_counter = 1

async def init_db():
    """Initialize in-memory database with sample data"""
    global service_id_counter, services_db
    
    # Comprehensive Klupa AI Services - Software-Level Drone Solutions
    services_db = [
        # 🔹 Drone Data Intelligence
        {
            "id": 1,
            "title": "AI-Powered Object Detection & Recognition",
            "slug": "ai-object-detection",
            "description": "Detect vehicles, people, crops, and anomalies with advanced AI algorithms",
            "category": "data_intelligence",
            "features": json.dumps([
                "Vehicle Detection & Classification",
                "People & Crowd Detection",
                "Crop Health Identification",
                "Anomaly Detection in Real-Time",
                "Multi-Class Object Recognition",
                "Custom Model Training",
                "Edge AI Processing",
                "Real-Time Alerting System"
            ]),
            "benefits": json.dumps([
                "Automated surveillance and monitoring",
                "Enhanced agricultural insights",
                "Reduced manual inspection time",
                "Increased safety and security",
                "Scalable detection capabilities"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 1,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 2,
            "title": "Change Detection Analysis",
            "slug": "change-detection",
            "description": "Compare past vs. present aerial images for construction, mining, and environmental monitoring",
            "category": "data_intelligence",
            "features": json.dumps([
                "Time-Series Image Comparison",
                "Automated Change Highlighting",
                "Volume Calculation (Cut/Fill)",
                "Progress Tracking Dashboard",
                "Environmental Impact Assessment",
                "Historical Archive Management",
                "Custom Alert Thresholds",
                "Export to GIS Formats"
            ]),
            "benefits": json.dumps([
                "Track construction progress accurately",
                "Monitor environmental changes",
                "Optimize mining operations",
                "Evidence-based decision making",
                "Regulatory compliance documentation"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": False,
            "order_index": 2,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 3,
            "title": "Thermal Image Analysis",
            "slug": "thermal-analysis",
            "description": "Powerline inspection, fire detection, and solar panel fault identification",
            "category": "data_intelligence",
            "features": json.dumps([
                "Powerline Hot Spot Detection",
                "Fire & Heat Signature Recognition",
                "Solar Panel Efficiency Analysis",
                "Building Heat Loss Mapping",
                "Temperature Anomaly Alerts",
                "Thermal Panorama Stitching",
                "Multi-Spectral Integration",
                "Automated Reporting"
            ]),
            "benefits": json.dumps([
                "Prevent powerline failures",
                "Early fire detection",
                "Maximize solar ROI",
                "Energy efficiency insights",
                "Predictive maintenance"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 3,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 4,
            "title": "3D Mapping & Reconstruction",
            "slug": "3d-mapping",
            "description": "Convert drone footage into accurate 3D terrain and building models using photogrammetry",
            "category": "data_intelligence",
            "features": json.dumps([
                "High-Resolution 3D Models",
                "Photogrammetry Processing",
                "Point Cloud Generation",
                "Mesh & Texture Mapping",
                "Elevation Map Creation",
                "Volume Measurements",
                "CAD/BIM Export",
                "VR/AR Compatibility"
            ]),
            "benefits": json.dumps([
                "Accurate site planning",
                "Digital twin creation",
                "Improved stakeholder visualization",
                "Precise volumetric analysis",
                "Reduced survey costs"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 4,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 5,
            "title": "Geospatial Analytics",
            "slug": "geospatial-analytics",
            "description": "Integrate drone data with GIS systems for advanced spatial analysis",
            "category": "data_intelligence",
            "features": json.dumps([
                "GIS Platform Integration",
                "Spatial Data Processing",
                "Multi-Layer Map Analysis",
                "Coordinate System Conversion",
                "NDVI & Vegetation Index",
                "Watershed & Terrain Analysis",
                "Custom Data Overlays",
                "ArcGIS & QGIS Support"
            ]),
            "benefits": json.dumps([
                "Comprehensive spatial insights",
                "Better land use planning",
                "Environmental monitoring",
                "Infrastructure optimization",
                "Data-driven policy making"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": False,
            "order_index": 5,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        
        # 🔹 Flight Management Software
        {
            "id": 6,
            "title": "Autonomous Flight Planning",
            "slug": "autonomous-flight-planning",
            "description": "AI-driven optimized routes for agriculture, surveillance, and delivery missions",
            "category": "flight_management",
            "features": json.dumps([
                "Intelligent Route Optimization",
                "Mission Planning Interface",
                "Terrain-Aware Path Generation",
                "Battery Life Prediction",
                "Weather Integration",
                "Multi-Waypoint Sequencing",
                "Return-to-Home Safeguards",
                "Mission Templates Library"
            ]),
            "benefits": json.dumps([
                "Maximized flight efficiency",
                "Reduced operational costs",
                "Extended coverage area",
                "Automated mission execution",
                "Increased mission success rate"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 6,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 7,
            "title": "Dynamic Obstacle Avoidance",
            "slug": "obstacle-avoidance",
            "description": "ML models for real-time obstacle detection and collision prevention",
            "category": "flight_management",
            "features": json.dumps([
                "Real-Time Obstacle Detection",
                "360° Sensor Fusion",
                "Predictive Path Adjustment",
                "Bird & Wildlife Avoidance",
                "Dynamic Re-Routing",
                "Vertical Obstacle Detection",
                "Low-Light Performance",
                "Fail-Safe Emergency Stop"
            ]),
            "benefits": json.dumps([
                "Enhanced flight safety",
                "Reduced crash risk",
                "Urban environment navigation",
                "All-weather operation",
                "Asset protection"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 7,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 8,
            "title": "Drone Swarm Management",
            "slug": "drone-swarm-management",
            "description": "Coordinate multiple drones with centralized management software",
            "category": "flight_management",
            "features": json.dumps([
                "Multi-Drone Coordination",
                "Centralized Command Center",
                "Formation Flying Algorithms",
                "Task Distribution AI",
                "Collision Avoidance Between Drones",
                "Real-Time Fleet Monitoring",
                "Synchronized Data Collection",
                "Scalable Architecture (10-1000+ drones)"
            ]),
            "benefits": json.dumps([
                "Large area coverage",
                "Parallel operations",
                "Redundancy and reliability",
                "Cost-effective scaling",
                "Complex mission execution"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 8,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 9,
            "title": "No-Fly Zone & Regulatory Compliance",
            "slug": "regulatory-compliance",
            "description": "Automatic restriction updates and airspace regulation integration",
            "category": "flight_management",
            "features": json.dumps([
                "Real-Time Airspace Updates",
                "Geo-Fencing Enforcement",
                "FAA/EASA Compliance",
                "TFR (Temporary Flight Restriction) Alerts",
                "Automatic Flight Permission",
                "Airport Proximity Warnings",
                "Custom Zone Configuration",
                "Audit Trail & Logs"
            ]),
            "benefits": json.dumps([
                "Regulatory compliance assured",
                "Avoid legal penalties",
                "Safe operation guarantees",
                "Automated restriction checks",
                "Peace of mind for operators"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": False,
            "order_index": 9,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        
        # 🔹 Cloud & Platform Services
        {
            "id": 10,
            "title": "Drone Data Cloud Platform",
            "slug": "cloud-platform",
            "description": "Store, process, and share drone footage with integrated analytics",
            "category": "cloud_platform",
            "features": json.dumps([
                "Unlimited Cloud Storage",
                "High-Speed Upload/Download",
                "Automated Processing Pipelines",
                "Collaborative Sharing",
                "Version Control",
                "Data Encryption at Rest",
                "Multi-User Access Management",
                "API Access for Developers"
            ]),
            "benefits": json.dumps([
                "Centralized data management",
                "Team collaboration",
                "Scalable infrastructure",
                "Secure data storage",
                "Global accessibility"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 10,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 11,
            "title": "Real-Time Video Streaming & AI Insights",
            "slug": "live-streaming-ai",
            "description": "Live drone feed with automatic tagging for security use cases",
            "category": "cloud_platform",
            "features": json.dumps([
                "HD/4K Live Streaming",
                "Low-Latency Transmission",
                "AI-Powered Auto-Tagging",
                "Event Detection & Alerts",
                "Multi-Viewer Support",
                "Recording & Playback",
                "Adaptive Bitrate Streaming",
                "Mobile & Web Clients"
            ]),
            "benefits": json.dumps([
                "Real-time situation awareness",
                "Instant threat detection",
                "Remote monitoring capability",
                "Evidence collection",
                "Enhanced security operations"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 11,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 12,
            "title": "API / SDK Services",
            "slug": "api-sdk-services",
            "description": "Developer tools to build applications on the Klupa AI drone platform",
            "category": "cloud_platform",
            "features": json.dumps([
                "RESTful API Access",
                "Python/JavaScript SDKs",
                "WebSocket Real-Time Data",
                "GraphQL Support",
                "Comprehensive Documentation",
                "Code Examples & Tutorials",
                "Sandbox Environment",
                "Developer Support Portal"
            ]),
            "benefits": json.dumps([
                "Custom application development",
                "Rapid integration",
                "Ecosystem expansion",
                "Third-party innovations",
                "Reduced development time"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": False,
            "order_index": 12,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 13,
            "title": "Drone Fleet Management Dashboard",
            "slug": "fleet-management",
            "description": "Track location, health, battery, and mission history of your drone fleet",
            "category": "cloud_platform",
            "features": json.dumps([
                "Real-Time Fleet Tracking",
                "Battery & Health Monitoring",
                "Mission History & Analytics",
                "Maintenance Scheduling",
                "Performance Metrics",
                "Multi-Location Support",
                "Custom Alerts & Notifications",
                "Asset Utilization Reports"
            ]),
            "benefits": json.dumps([
                "Optimized fleet operations",
                "Reduced downtime",
                "Predictive maintenance",
                "Cost tracking",
                "Improved asset lifespan"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 13,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        
        # 🔹 Security & Safety Software
        {
            "id": 14,
            "title": "Encrypted Communication Protocols",
            "slug": "encrypted-communications",
            "description": "Secure drone-to-controller data transmission with military-grade encryption",
            "category": "security_safety",
            "features": json.dumps([
                "AES-256 Encryption",
                "End-to-End Security",
                "Secure Command & Control",
                "Anti-Jamming Technology",
                "Frequency Hopping",
                "Certificate-Based Authentication",
                "Intrusion Detection",
                "Secure Firmware Updates"
            ]),
            "benefits": json.dumps([
                "Data confidentiality",
                "Prevent unauthorized access",
                "Mission integrity",
                "Compliance with security standards",
                "Protection against cyber threats"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 14,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 15,
            "title": "Cybersecurity Patches as a Service",
            "slug": "cybersecurity-patches",
            "description": "Recurring security updates for client drone fleets",
            "category": "security_safety",
            "features": json.dumps([
                "Automated Patch Deployment",
                "Zero-Day Vulnerability Protection",
                "Scheduled Update Windows",
                "Rollback Capabilities",
                "Compliance Reporting",
                "Security Audit Logs",
                "Multi-Fleet Management",
                "24/7 Security Monitoring"
            ]),
            "benefits": json.dumps([
                "Always up-to-date security",
                "Reduced attack surface",
                "Regulatory compliance",
                "Minimal operational disruption",
                "Proactive threat mitigation"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 15,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 16,
            "title": "Anomaly Detection in Flight",
            "slug": "flight-anomaly-detection",
            "description": "Detect if a drone is hijacked or behaving abnormally during operation",
            "category": "security_safety",
            "features": json.dumps([
                "Behavioral Pattern Analysis",
                "Hijack Detection",
                "GPS Spoofing Detection",
                "Abnormal Movement Alerts",
                "Communication Loss Detection",
                "Automatic Emergency Response",
                "Flight Data Black Box",
                "Forensic Analysis Tools"
            ]),
            "benefits": json.dumps([
                "Enhanced security",
                "Early threat detection",
                "Asset protection",
                "Incident investigation",
                "Operator safety"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": False,
            "order_index": 16,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 17,
            "title": "Drone Identity Management (Remote-ID)",
            "slug": "drone-identity",
            "description": "Authenticate and track drones with Remote-ID compliance",
            "category": "security_safety",
            "features": json.dumps([
                "FAA Remote-ID Compliance",
                "Unique Drone Identification",
                "Real-Time Location Broadcasting",
                "Operator Registration",
                "Flight Authority Verification",
                "Network & Broadcast Remote-ID",
                "Digital Certificate Management",
                "Airspace Accountability"
            ]),
            "benefits": json.dumps([
                "Regulatory compliance",
                "Public safety enhancement",
                "Law enforcement cooperation",
                "Authorized operations only",
                "Trust and transparency"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": False,
            "order_index": 17,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        
        # 🔹 Industry-Specific Solutions
        {
            "id": 18,
            "title": "Agriculture: Crop Health & Yield Prediction",
            "slug": "agriculture-solutions",
            "description": "Crop health analysis, yield prediction, and automated spraying software",
            "category": "industry_specific",
            "features": json.dumps([
                "NDVI Crop Health Mapping",
                "Disease Detection AI",
                "Yield Prediction Models",
                "Precision Spraying Control",
                "Irrigation Optimization",
                "Soil Analysis Integration",
                "Multi-Season Comparison",
                "Farm Management Integration"
            ]),
            "benefits": json.dumps([
                "Increased crop yields",
                "Reduced chemical usage",
                "Early disease detection",
                "Cost savings",
                "Sustainable farming practices"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 18,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 19,
            "title": "Smart Cities: Crowd & Traffic Analytics",
            "slug": "smart-cities",
            "description": "Crowd density analytics and traffic monitoring dashboards for urban management",
            "category": "industry_specific",
            "features": json.dumps([
                "Real-Time Crowd Counting",
                "Traffic Flow Analysis",
                "Congestion Prediction",
                "Event Monitoring Dashboard",
                "Parking Availability Detection",
                "Incident Detection & Response",
                "Heatmap Visualization",
                "Integration with City Systems"
            ]),
            "benefits": json.dumps([
                "Improved public safety",
                "Traffic optimization",
                "Event planning insights",
                "Emergency response efficiency",
                "Smart city operations"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 19,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 20,
            "title": "Logistics: Delivery Drone Optimization",
            "slug": "logistics-delivery",
            "description": "Route optimization for delivery drones with payload monitoring",
            "category": "industry_specific",
            "features": json.dumps([
                "Last-Mile Delivery Optimization",
                "Multi-Stop Route Planning",
                "Payload Weight Management",
                "Delivery Verification (Photo/GPS)",
                "Weather-Adaptive Routing",
                "Customer Notification System",
                "Return-to-Hub Automation",
                "Fleet Efficiency Analytics"
            ]),
            "benefits": json.dumps([
                "Faster deliveries",
                "Reduced delivery costs",
                "Increased delivery capacity",
                "Customer satisfaction",
                "Carbon footprint reduction"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 20,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": 21,
            "title": "Disaster Response: Search & Rescue AI",
            "slug": "disaster-response",
            "description": "AI models for missing person detection, flood/fire mapping dashboards",
            "category": "industry_specific",
            "features": json.dumps([
                "Missing Person Detection AI",
                "Heat Signature Search",
                "Flood Extent Mapping",
                "Fire Perimeter Tracking",
                "Structural Damage Assessment",
                "Emergency Communication Relay",
                "Real-Time Situational Reports",
                "Multi-Agency Coordination"
            ]),
            "benefits": json.dumps([
                "Faster rescue operations",
                "Life-saving capabilities",
                "Improved disaster assessment",
                "Resource allocation optimization",
                "Enhanced emergency response"
            ]),
            "icon": None,
            "image_url": None,
            "is_featured": True,
            "order_index": 21,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
    ]
    
    service_id_counter = 22
    print("✅ In-memory database initialized with comprehensive Klupa AI services")

# Helper functions for data access
def get_next_id(counter_name: str) -> int:
    """Get next ID for a counter"""
    global service_id_counter, contact_id_counter, demo_id_counter, patch_id_counter
    
    if counter_name == "service":
        result = service_id_counter
        service_id_counter += 1
    elif counter_name == "contact":
        result = contact_id_counter
        contact_id_counter += 1
    elif counter_name == "demo":
        result = demo_id_counter
        demo_id_counter += 1
    elif counter_name == "patch":
        result = patch_id_counter
        patch_id_counter += 1
    else:
        result = 1
    
    return result
