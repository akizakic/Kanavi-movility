% 주어진 CSV 파일의 경로와 파일명 설정
file_path = 'C:\Users\user\Desktop\Kanavi\Data\rain_object (2).csv';

% 데이터 불러오기
opts = detectImportOptions(file_path); % 데이터 불러오기 옵션 설정
opts.VariableNamingRule = 'preserve';  % 'preserve'로 설정하여 원본 열 제목 유지
data = readtable(file_path, opts);     % 설정된 옵션으로 데이터 불러오기

% 모든 짝수행 데이터 추출
even_rows = 2:2:size(data, 1); % 짝수 행 선택 (1에서 시작하며 2씩 증가)
data_subset = data(even_rows, :);

% 모든 홀수행 데이터 추출
odd_rows = 1:2:size(data, 1); % 홀수 행 선택 (1에서 시작하며 2씩 증가)
data_subset_odd = data(odd_rows, :);

% 데이터 처리 (심하게 변화하는 값을 제거)
threshold = 10; % 변화가 큰 임계값 설정
processed_data = data_subset; % 초기화
for col = 2:width(processed_data)
    column_data = processed_data{:, col};
    % 변화가 큰 값을 찾아 NaN으로 대체
    diff_values = abs(diff(column_data));
    outlier_indices = find(diff_values > threshold) + 1;
    column_data(outlier_indices) = NaN;
    processed_data{:, col} = column_data;
end

%홀수행 데이터 처리
threshold = 10; % 변화가 큰 임계값 설정
processed_data_odd = data_subset_odd; % 초기화
for col = 2:width(processed_data_odd)
    column_data = processed_data_odd{:, col};
    % 변화가 큰 값을 찾아 NaN으로 대체
    diff_values = abs(diff(column_data));
    outlier_indices = find(diff_values > threshold) + 1;
    column_data(outlier_indices) = NaN;
    processed_data_odd{:, col} = column_data;
end


% 이후의 원통형 좌표계 변환과 그래프 그리기 부분은 이전 코드와 동일하게 유지합니다.

% 원통형 좌표계 변환
angles = 0:0.25:120;
distances = processed_data{end-9, 2:end};
theta = deg2rad(angles);
x = distances .* cos(theta);
y = distances .* sin(theta);

% odd
angles = 0:0.25:120;
distances_odd = processed_data_odd{end-9, 2:end};
theta = deg2rad(angles);
x_odd = distances_odd .* cos(theta);
y_odd = distances_odd .* sin(theta);

% 방의 바닥 높이 2channel
floor_height = 0;
floor_height_odd = 1;


% 3D 그래프 그리기 (전체 짝수행 및 홀수행 데이터)
figure('Units','Normalized','OuterPosition',[0 0 1 1]);


% 전체 데이터 그리기
scatter3(x, y, ones(size(x)) * floor_height, 'filled', 'MarkerFaceColor', 'b');
xlabel('X축');
ylabel('Y축');
zlabel('Z축');
title('3D - 전체 데이터');

hold on;

% 홀수행 데이터 그리기
scatter3(x_odd, y_odd, ones(size(x_odd)) * floor_height_odd, 'filled', 'MarkerFaceColor', 'r');

hold off;

% 
% hold on;
% 
% % 홀수행 데이터 그리기
% for i = 1:size(processed_data_odd, 1)
%     distances_subset_odd = processed_data_odd{i, 2:end};
%     x_subset_odd = distances_subset_odd .* cos(theta);
%     y_subset_odd = distances_subset_odd .* sin(theta);
%     scatter3(x_subset_odd, y_subset_odd, ones(size(x_subset_odd)) * floor_height_odd, 'filled', 'MarkerFaceColor', 'r');
% end
% 
% hold off;




% 모든 짝수행 데이터를 추출하여 3D 그래프 그리기

figure('Units','Normalized','OuterPosition',[0 0 1 1]);

hold on;
for i = 1:size(processed_data, 1)
    distances_subset = processed_data{i, 2:end};
    x_subset = distances_subset .* cos(theta);
    y_subset = distances_subset .* sin(theta);
    

    scatter3(x_subset, y_subset, ones(size(x_subset)) * floor_height, 'filled', 'MarkerFaceColor', 'b');
end

xlabel('X축');
ylabel('Y축');
zlabel('Z축');
title('3D - 짝수행 데이터');
view(3);
hold off;


% 모든 홀수행 데이터를 추출하여 3D 그래프 그리기
figure('Units','Normalized','OuterPosition',[0 0 1 1]);
hold on;
for i = 1:size(processed_data_odd, 1)
    distances_subset_odd = processed_data_odd{i, 2:end};
    x_subset_odd = distances_subset_odd .* cos(theta);
    y_subset_odd = distances_subset_odd .* sin(theta);
    scatter3(x_subset_odd, y_subset_odd, ones(size(x_subset_odd)) * floor_height_odd, 'filled', 'MarkerFaceColor', 'r');
    xlabel('X축');
    ylabel('Y축');
    zlabel('Z축');
    title(['3D - 홀수행 데이터 (Row ', num2str(odd_rows(i)), ')']);
end
view(3);

hold off;

% % 3D 그래프 그리기 (전체 데이터)
% figure('Units','Normalized','OuterPosition',[0 0 1 1]);
% scatter3(x, y, ones(size(x)) * floor_height, 'filled', 'MarkerFaceColor', 'b');
% xlabel('X축');
% ylabel('Y축');
% zlabel('Z축');
% title('3D - 선별한 데이터');


%  for i = 2:2:size(processed_data, 1)
%      distances_subset = processed_data{i, 2:end}; % 여기서도 processed_data로 수정
%      x_subset = distances_subset .* cos(theta);
%      y_subset = distances_subset .* sin(theta);
%      
%      % 새로운 figure로 3D 그래프 띄우기
%      figure('Units','Normalized','OuterPosition',[0 0 1 1]);
%      scatter3(x_subset, y_subset, ones(size(x_subset)) * floor_height, 'filled', 'MarkerFaceColor', 'r');
%      hold on;
%  end
%  hold off;
% 
%      xlabel('X축');
%      ylabel('Y축');
%      zlabel('Z축');
%      title(['3D - 짝수행 데이터 (Row ', num2str(i), ')']);
     
 


% 3D 그래프 그리기 (1에서 50행 중 짝수행만)
% figure('Units','Normalized','OuterPosition',[0 0 1 1]); % 전체 화면으로 띄우기
% for i = even_rows
%     distances_subset = processed_data{i, 2:end}; % 여기서도 processed_data로 수정
%     x_subset = distances_subset .* cos(theta);
%     y_subset = distances_subset .* sin(theta);
%     scatter3(x_subset, y_subset, ones(size(x_subset)) * floor_height, 'filled', 'MarkerFaceColor', 'r');
%     hold on;
% end
% hold off; % 모든 그래프를 그린 후 hold off로 설정하여 다음 그래프는 새로운 figure에 그려지도록 합니다.
% xlabel('X-axis');
% ylabel('Y-axis');
% zlabel('Z-axis');
% title('3D - 짝수행 데이터');


% for i = even_rows
%     distances_subset = processed_data{i, 2:end}; % 여기서도 processed_data로 수정
%     x_subset = distances_subset .* cos(theta);
%     y_subset = distances_subset .* sin(theta);
%     
%     % 새로운 figure로 3D 그래프 띄우기
%     figure('Units','Normalized','OuterPosition',[0 0 1 1]);
%     scatter3(x_subset, y_subset, ones(size(x_subset)) * floor_height, 'filled', 'MarkerFaceColor', 'r');
%     xlabel('X-axis');
%     ylabel('Y-axis');
%     zlabel('Z-axis');
%     title(['3D - 짝수행 데이터 (Row ', num2str(i), ')']);
% end

