**Database Schema**

## `users` table

| Column Name | Data Type | Details |
|-------------|-----------|---------|
| id          | integer   | Primary Key |
| username    | string    | |
| email       | string    | Indexed, Unique |
| password    | string    | Hashed/Encrypted |
| created_at  | datetime  | |
| updated_at  | datetime  | |

## `channels` table

| Column Name | Data Type | Details |
|-------------|-----------|---------|
| id          | integer   | Primary Key |
| user_id     | integer   | Foreign Key referencing `users` table |
| title       | string    | |
| description | string    | |
| category_id | integer   | Foreign Key referencing `categories` table |
| created_at  | datetime  | |
| updated_at  | datetime  | |

## `categories` table

| Column Name | Data Type | Details |
|-------------|-----------|---------|
| id          | integer   | Primary Key |
| name        | string    | |

## `vods` table

| Column Name | Data Type | Details |
|-------------|-----------|---------|
| id          | integer   | Primary Key |
| channel_id  | integer   | Foreign Key referencing `channels` table |
| title       | string    | |
| description | string    | |
| tags        | string    | |
| upload_time | datetime  | |
| video_url   | string    | |

## `followers` table

| Column Name | Data Type | Details |
|-------------|-----------|---------|
| id          | integer   | Primary Key |
| user_id     | integer   | Foreign Key referencing `users` table |
| channel_id  | integer   | Foreign Key referencing `channels` table |

## `comments` table

| Column Name | Data Type | Details |
|-------------|-----------|---------|
| id          | integer   | Primary Key |
| vod_id      | integer   | Foreign Key referencing `vods` table |
| user_id     | integer   | Foreign Key referencing `users` table |
| content     | string    | |
| created_at  | datetime  | |
| updated_at  | datetime  | |
