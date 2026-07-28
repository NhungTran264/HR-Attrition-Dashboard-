# Phân Tích Nghỉ Việc Nhân Sự (HR Attrition Analysis)

## Tổng Quan Project
Project này phân tích bộ dữ liệu **IBM HR Analytics Attrition** bằng **Power BI** nhằm xác định các yếu tố chính ảnh hưởng đến tình trạng nghỉ việc của nhân viên. Mục tiêu là tìm ra các xu hướng theo phòng ban, nhân khẩu học, mức thu nhập và điều kiện làm việc, từ đó hỗ trợ bộ phận Nhân sự ra quyết định dựa trên dữ liệu.

---

## Công Cụ Sử Dụng
- Power BI Desktop
- DAX (Data Analysis Expressions)
- Power Query

---

## Câu Hỏi Phân Tích Chính
- Phòng ban và vị trí công việc nào có tỷ lệ nghỉ việc cao nhất?
- Độ tuổi, giới tính và tình trạng hôn nhân liên quan như thế nào đến việc nghỉ việc?
- Mức thu nhập có ảnh hưởng đến tỷ lệ nghỉ việc không?
- Làm thêm giờ (overtime) và đi công tác ảnh hưởng như thế nào đến việc nghỉ việc?
- Nhân viên thường nghỉ việc nhiều nhất vào giai đoạn nào trong thời gian làm việc tại công ty?

---

## Các Chỉ Số KPI Chính
- Tổng số nhân viên: **1.470**
- Số lượng nghỉ việc: **237**
- Tỷ lệ nghỉ việc: **16,12%**
- Thu nhập trung bình/tháng: **$6,5K**
- Độ tuổi trung bình: **36,92**
- Số năm làm việc trung bình: **7,0**

---

## Tính Năng Dashboard
**Trang Overview (Tổng quan)**
- Các KPI toàn công ty (Tổng nhân viên, Số lượng nghỉ việc, Tỷ lệ nghỉ việc, Thu nhập TB, Tuổi TB)
- Tỷ lệ nghỉ việc theo Phòng ban, Giới tính, Nhóm tuổi
- Tỷ lệ nghỉ việc theo Tần suất công tác, Làm thêm giờ, Mức độ hài lòng công việc

**Trang Attrition Analysis (Phân tích nghỉ việc)**
- Tỷ lệ nghỉ việc theo Vị trí công việc và Tình trạng hôn nhân
- Xu hướng nghỉ việc theo số năm làm việc tại công ty
- Tỷ lệ nghỉ việc theo nhóm thu nhập

**Trang Employee Profile (Hồ sơ nhân viên)**
- Thu nhập trung bình, Tuổi trung bình, Số năm làm việc trung bình
- Thu nhập trung bình theo Phòng ban
- Tổng số nhân viên theo Nhóm tuổi và Mức độ cân bằng công việc - cuộc sống

Bộ lọc tương tác (Phòng ban, Vị trí công việc) cùng hệ thống điều hướng bằng nút bấm (bookmark navigation) giúp người dùng chuyển đổi linh hoạt giữa 3 trang dashboard.
---

## Phát Hiện Chính (Key Findings)
- Phòng **Research & Development** ghi nhận số lượng nghỉ việc cao nhất (133 người), tiếp theo là Sales (92 người). → Gợi ý: cần rà soát thêm tỷ lệ nghỉ việc theo % trên tổng nhân sự từng phòng để xác định phòng ban thực sự có "vấn đề" thay vì chỉ do quy mô đông người.
- Nhân viên **độc thân** có tỷ lệ nghỉ việc cao nhất (50,63%), so với đã kết hôn (35,44%) và ly hôn (13,92%). → Gợi ý: nhóm độc thân thường linh hoạt hơn trong việc chuyển việc, có thể cân nhắc chính sách giữ chân riêng cho nhóm này.
- Tỷ lệ nghỉ việc tăng vọt trong **năm đầu tiên** làm việc (59 trường hợp), sau đó giảm mạnh từ năm thứ 2 trở đi. → Gợi ý: nên đầu tư vào chương trình onboarding và hỗ trợ nhân viên mới trong 12 tháng đầu để giảm attrition sớm.
- Nhân viên có thu nhập dưới **$3.000/tháng** có tỷ lệ nghỉ việc cao nhất (113 người), giảm dần khi thu nhập tăng. → Gợi ý: xem xét lại chính sách lương khởi điểm cho nhóm thu nhập thấp.
- **Laboratory Technician** là vị trí có số lượng nghỉ việc cao nhất (62 người), tiếp theo là Sales Executive (57 người).
- Nhân viên có **làm thêm giờ** có số lượng nghỉ việc cao hơn (127) so với nhóm không làm thêm giờ (110) — đây là một trong những chỉ báo nghỉ việc mạnh nhất trong bộ dữ liệu. → Gợi ý: cần đánh giá lại khối lượng công việc và chính sách overtime tại các phòng ban có tần suất OT cao.
- Nhân viên có **tần suất công tác thường xuyên** chiếm tỷ trọng nghỉ việc cao hơn (29% trong tổng số người nghỉ việc) so với nhóm không đi công tác (5%), dù nhóm "Travel Rarely" chiếm tỷ trọng lớn nhất trong tổng số nhân viên. (Lưu ý: đây là tỷ lệ % trên tổng số người đã nghỉ việc, không phải % nghỉ việc trong từng nhóm.)
- Phần lớn nhân viên đánh giá mức độ cân bằng công việc - cuộc sống ở mức **"Better"** (893 người), cho thấy điều kiện làm việc nhìn chung khá tốt trên toàn công ty.
---
## Phân Tích Dự Đoán (Predictive Modeling)

Để kiểm chứng và mở rộng thêm các insight từ dashboard Power BI, mình đã xây dựng thêm một mô hình dự đoán attrition bằng **Python (scikit-learn)**.

**Phương pháp**
- Tiền xử lý: mã hóa one-hot cho các biến phân loại (Department, JobRole, OverTime...), chia dữ liệu train/test theo tỷ lệ 80/20 (giữ nguyên tỷ lệ Attrition giữa 2 tập bằng `stratify`).
- Mô hình sử dụng: **Random Forest Classifier** (200 cây), có áp dụng `class_weight='balanced'` để giảm ảnh hưởng của dữ liệu mất cân bằng (chỉ ~16% nhân viên nghỉ việc).

**Kết quả đánh giá mô hình**

| Chỉ số | Nhóm "Không nghỉ việc" | Nhóm "Nghỉ việc" |
|---|---|---|
| Precision | 0.87 | 0.42 |
| Recall | 0.93 | 0.28 |
| F1-score | 0.90 | 0.33 |

- **ROC-AUC: 0.78** — cho thấy mô hình có khả năng phân biệt tốt giữa nhân viên có nguy cơ nghỉ việc và nhân viên ở lại, cao hơn đáng kể so với đoán ngẫu nhiên (0.5).
- Recall ở nhóm "Nghỉ việc" còn thấp (0.28), điều này phản ánh đúng đặc điểm dữ liệu: chỉ có 237/1.470 nhân viên nghỉ việc, khiến mô hình có ít mẫu để học tốt nhóm thiểu số này. Đây là hạn chế cố hữu của bài toán, không phải lỗi triển khai.
- Không sử dụng **Accuracy (0.82)** làm chỉ số chính vì bị "ảo" bởi nhóm đa số (No) chiếm phần lớn dữ liệu.

**Top 10 Yếu Tố Ảnh Hưởng Đến Attrition (Feature Importance)**

1. Monthly Income
2. Age
3. Total Working Years
4. Daily Rate*
5. Years At Company
6. OverTime
7. Monthly Rate*
8. Hourly Rate*
9. Distance From Home
10. Years With Current Manager

*Lưu ý: Daily Rate, Monthly Rate, Hourly Rate là các trường có tính chất dữ liệu không rõ ràng về mặt nghiệp vụ trong bộ dữ liệu gốc, nên được diễn giải thận trọng và không dùng làm cơ sở đề xuất chính sách.

**Đối chiếu với Dashboard Power BI**

Kết quả từ mô hình dự đoán **đồng nhất với các insight từ phân tích mô tả** trên Power BI:
- **Monthly Income** là yếu tố dự đoán mạnh nhất → khớp với phát hiện "nhân viên thu nhập dưới $3.000/tháng có tỷ lệ nghỉ việc cao nhất".
- **OverTime** nằm trong top 6 → xác nhận lại insight "làm thêm giờ là một trong những chỉ báo nghỉ việc mạnh nhất".
- **Age** và **Years At Company** cũng nằm trong top → khớp với xu hướng "attrition tập trung ở nhân viên trẻ và mới vào năm đầu tiên".

Việc hai phương pháp phân tích độc lập (BI mô tả và Machine Learning dự đoán) cho ra cùng một nhóm insight giúp củng cố độ tin cậy của kết quả phân tích tổng thể.
---

## Kết Quả Project
Dashboard này xác định các yếu tố chính dẫn đến nghỉ việc — bao gồm **mức thu nhập, vị trí công việc, thời gian làm việc và làm thêm giờ** — giúp bộ phận Nhân sự có cơ sở dữ liệu cụ thể để xây dựng **chiến lược giữ chân nhân viên** cho các nhóm có rủi ro nghỉ việc cao.

---

## Nguồn Dữ Liệu
IBM HR Analytics Attrition Dataset (Kaggle)
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
