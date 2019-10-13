------------USERS

USE [Seminotti]
GO

/****** Object:  Table [dbo].[User]    Script Date: 10/10/2019 18:04:52 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[User](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[Nome] [varchar](250) NOT NULL,
	[Sobrenome] [varchar](250) NOT NULL,
	[UserName] [varchar](250) NOT NULL,
	[Password] [varchar](250) NOT NULL,
	[Type] [int] NOT NULL,
	[email] [varchar](250) NOT NULL,
	[Phone] [varchar](15) NULL,
 CONSTRAINT [PK_User] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

----------------- categoria

USE [Seminotti]
GO

/****** Object:  Table [dbo].[PostCategory]    Script Date: 10/10/2019 18:03:47 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[PostCategory](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[Name] [varchar](50) NOT NULL,
	[Descricao] [varchar](50) NOT NULL,
	[Type] [int] NOT NULL,
	[InsertDate] [datetime] NOT NULL,
 CONSTRAINT [PK_PostCategory] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[PostCategory] ADD  CONSTRAINT [DF_PostCategory_InsertDate]  DEFAULT (getdate()) FOR [InsertDate]
GO


------------------Post 


USE [Seminotti]
GO

/****** Object:  Table [dbo].[Post]    Script Date: 10/10/2019 18:05:41 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Post](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[Titulo] [varchar](100) NOT NULL,
	[Descricao] [varchar](250) NULL,
	[Conteudo] [text] NOT NULL,
	[Status] [int] NOT NULL,
	[DataInicial] [datetime] NOT NULL,
	[DataFinal] [datetime] NOT NULL,
	[DataCriacao] [datetime] NOT NULL,
	[UserPostId] [bigint] NOT NULL,
	[Category_ID] [bigint] NOT NULL,
 CONSTRAINT [PK_Post] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[Post]  WITH CHECK ADD  CONSTRAINT [FK_Post_Post] FOREIGN KEY([UserPostId])
REFERENCES [dbo].[User] ([id])
GO

ALTER TABLE [dbo].[Post] CHECK CONSTRAINT [FK_Post_Post]
GO

ALTER TABLE [dbo].[Post]  WITH CHECK ADD  CONSTRAINT [FK_Post_PostCategory] FOREIGN KEY([Category_ID])
REFERENCES [dbo].[PostCategory] ([Id])
GO

ALTER TABLE [dbo].[Post] CHECK CONSTRAINT [FK_Post_PostCategory]
GO


----------- iMagens


USE [Seminotti]
GO

/****** Object:  Table [dbo].[Imagens]    Script Date: 10/10/2019 18:06:05 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Imagens](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[Image] [text] NOT NULL,
	[Insertdate] [datetime] NOT NULL,
	[Post_ID] [bigint] NOT NULL,
 CONSTRAINT [PK_Imagens] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

ALTER TABLE [dbo].[Imagens] ADD  CONSTRAINT [DF_Imagens_Insertdate]  DEFAULT (getdate()) FOR [Insertdate]
GO

ALTER TABLE [dbo].[Imagens]  WITH CHECK ADD  CONSTRAINT [FK_Imagens_Post] FOREIGN KEY([Post_ID])
REFERENCES [dbo].[Post] ([Id])
GO

ALTER TABLE [dbo].[Imagens] CHECK CONSTRAINT [FK_Imagens_Post]
GO



